from z3 import *
import itertools, collections

class SolverGen:
    def __init__(self):
        self.varCount = 0
    def genVar(self, i):
        self.varCount += 1
        return Int("%s_%d" % ("abc"[i], self.varCount))
    def addSolver(self, solver, i, n, vs):
        if i == 0: return
        myIndex, unknownIndex = (i + 2) % 3, (i + 1) % 3
        oldvs = vs[:unknownIndex] + vs[unknownIndex+1:]
        tmpvs = [self.genVar(unknownIndex) for j in range(3)]
        for j in range(3):
            solver.add(And(1 <= tmpvs[j], tmpvs[j] <= n))
            solver.add([tmpvs[j] != y for y in oldvs])
            xs1 = vs[:unknownIndex] + [tmpvs[j]] + vs[unknownIndex+1:]
            x1, y1, z1 = xs1[j:] + xs1[:j]
            solver.add(Or(And(y1 < x1, x1 < z1), And(z1 < x1, x1 < y1)))
            self.addSolver(solver, i - 1, n, xs1)
        return
    def makeSolver(self, i, n):
        solver = Solver()
        vs = [Int(x) for x in 'abc']
        solver.add([And(1 <= x, x <= n) for x in vs])
        solver.add([x != y for x, y in itertools.combinations(vs, 2)])
        for j in range(i + 1):
            self.addSolver(solver, j, n, vs)
        return solver
n = 20
for i in range(20):
    solver = SolverGen().makeSolver(i, n)
    if solver.check() == sat:
        print(i)
        print(solver)
        print(solver.model())
    else:
        break
