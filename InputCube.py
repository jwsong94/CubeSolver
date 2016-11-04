import pycuber as pc
from pycuber.solver import CFOPSolver

#input -> Left, Top, Front, Button, Right, Back
#0-r, 1-y, 2-g, 3-w, 4-o, 5-b
#input
#123
#456
#789

#mycube = pc.Cube(pc.array_to_cubies("000000000111111111222222222333333333444444444555555555"))

mycub2 = pc.Cube(pc.array_to_cubies("040404040131313131252525252313131313404040404525252525"))

#mycube("R U R' U'")

#print(mycube)
mycub2("")
print(mycub2)
#print(mycub2)

solver = CFOPSolver(mycub2)
solution = solver.solve(suppress_progress_messages=True)
print(solution)
#print(solver)
#solver.solve()
#print(mycub2)

#c = pc.Cube()
#alg = pc.Formula()
#random_alg = alg.random()
#c(random_alg)
#solver = CFOPSolver(c)
#solver.solve()

