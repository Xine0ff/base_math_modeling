import math
print(math.sqrt(3))

import sympy
print(sympy.sqrt(3))
print(2*sympy.sqrt(3))

from sympy import symbols
x,y,z=symbols('x y z')
expr=x+2*y
print(expr)
print(expr+1)
print(expr*x)

from sympy import sin,cos,pi,exp
print(sin(x**2)-exp(-2*x)+cos(pi/x))

expr=sin(x**2)-exp(-2*x)+cos(pi/x)
expr_new=expr.subs(x,y)
print(expr_new)
expr_new=expr.subs(x,pi)
print(expr_new)
expr_num=expr_new.evalf()
print(expr_num)

expr_new=expr.subs(x,x**2)
print(expr_new)

expr=x**3+4*x*y-z
expr_new=expr.subs([(x,2),(y,4),(z,0)])
print(expr_new)

#simplify, expand, factor
from sympy import simplify, expand, factor, trigsimp

simp_expr=simplify(sin(x)**2+cos(x)**2)
print(simp_expr)

simp_expr=simplify((x**3+x**2-x-1)/(x**2+2*x+1))
print(simp_expr)

simp_expr=expand((x+1)**22)
print(simp_expr)

simp_expr=expand((x+2)*(x-3))
print(simp_expr)

simp_expr=expand((x+1)*(x-2)-(x-1)*x)
print(simp_expr)

simp_expr=factor(x**3-x**2+x-1)
print(simp_expr)

simp_expr=trigsimp(sin(x)**2 +cos(x)**2)
print(simp_expr)

simp_expr=trigsimp(sin(x)**4-2*cos(x)**2*sin(x)**2+cos(x)**4)
print(simp_expr)

#
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

expr=2*x**2-2
solve_expr=solve(expr,x)
print(solve_expr)

expr=Eq(x,y)
print(expr)

expr=Eq(3,1)
print(expr)

expr=Eq(3,3)
print(expr)

system=[x+y+z-1,x+y+2*z-3,x-2*y+z]
solve_system=linsolve(system,(x,y,z))
print(solve_system)

system=[x**2+x,x-y]
solve_system=nonlinsolve(system,[x,y])
print(solve_system)

system=[x**2+1,y**2+1]
solve_system=nonlinsolve(system,[x,y])
print(solve_system)

system=[x**2-2*y**2-2,x*y-2]
solve_system=nonlinsolve(system,[x,y])
print(solve_system)