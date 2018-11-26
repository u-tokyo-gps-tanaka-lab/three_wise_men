from z3 import *
import itertools
for n in range(10):
    solver = Solver()
    vs = [Int("a"), Int("b"), Int("c")]
    solver.add([x != y for x, y in itertools.combinations(vs, 2)])
    solver.add([And(1 <= x, x <= n) for x in vs])
    if solver.check() == sat:
        print("n = %d" % n)
        print(solver)
        print(solver.model())
        break
