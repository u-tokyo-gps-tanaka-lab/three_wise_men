from z3 import *
import itertools, collections
for n in range(10):
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
    if solver.check() == sat:
        print("n = %d" % n)
        print(solver)
        print(solver.model())
        break
