from z3 import *
#                x0
#            x11 x12 x1
#        x10 x17     x13 x2
#        x9      x18     x3
#        x8  x16     x14 x4
#            x7  x15  x5
#                x6 
n = 19
for m in range(22, 39):
    xs = [Int("x%d" % i) for i in range(n)]
    solver=Solver()
    solver.add([And(1 <= x, x <= n) for x in xs])
    solver.add(Distinct(xs))
    for i in range(6):
        solver.add(xs[i * 2] + xs[i * 2 + 1] + xs[(i * 2 + 2) % 12] == m)
        solver.add(xs[i * 2] + xs[12 + i] + xs[18] == m)
    solver.add([xs[0] < xs[2 * i] for i in range(1, 6)])
    solver.add(xs[2] < xs[10])
    r = []
    while solver.check() == sat:
        model = solver.model()
        r.append([model[xs[i]] for i in range(n)])
        solver.add(Or([x != model[x] for x in xs]))
    print("%d %d %s" %(m, len(r), r))
