from z3 import *
import itertools, collections
for n in range(20):
    solver = Solver()
    v = [Int("a"), Int("b"), Int("c")]
    solver.add([x != y for x, y in itertools.combinations(v, 2)])
    cs = [Int("c_0"), Int("c_1"), Int("c_2")]
    solver.add([And(1 <= x, x <= n) for x in v + cs])
    solver.add([And(v[0] != x, v[1] != x) for x in cs])
    for i in range(3):
        xs = [v[0], v[1], cs[i]]
        x, y, z = xs[i:] + xs[:i]
        solver.add(Or(And(y < x, x < z), And(z < x, x < y)))
    a = [Int("a_0"), Int("a_1"), Int("a_2")]
    solver.add([And(1 <= x, x <= n) for x in a])
    solver.add([And(v[1] != x, v[2] != x) for x in a])
    for i in range(3):
        xs = [a[i], v[1], v[2]]
        x, y, z = xs[i:] + xs[:i]
        solver.add(Or(And(y < x, x < z), And(z < x, x < y)))
        cs1 = [Int("c_%d_%d" % (i, j)) for j in range(3)]
        solver.add([And(1 <= x, x <= n) for x in cs1])
        solver.add([And(v[0] != x, v[1] != x) for x in cs1])
        for j in range(3):
            xs1 = [a[i], v[1], cs1[j]]
            x1, y1, z1 = xs1[j:] + xs1[:j]
            solver.add(Or(And(y1 < x1, x1 < z1), And(z1 < x1, x1 < y1)))
    if solver.check() == sat:
        print("n = %d" % n)
        print(solver)
        print(solver.model())
        break

