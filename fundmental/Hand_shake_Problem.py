from sympy import symbols, solve
import math import ceil, sqrt
# handshakes = 7
# x = symbols('x')
# expr = x**2 - x -handshakes*2
# sol = solve(expr)
# for i in sol:
#     if math.ceil(i) > 0:
#         print(math.ceil(i))

n = 6
if n > 0:
    print(ceil((1 + sqrt( 1 + 8 * n)) / 2))