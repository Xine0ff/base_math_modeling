from sympy import symbols
x,y,z=symbols('x y z')
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy import sin,cos,pi,exp
from sympy import simplify, expand, factor, trigsimp
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs

sol1=reduce_abs_inequality(Abs(x**2+2*x-3)+3*(x+1),'<',x)
print(sol1)

sol2=reduce_rational_inequalities( [[((x-1)*(x+2))/((x-3)*(x+4))<=0]],x )
print(sol2)