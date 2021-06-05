import sympy
from sympy import symbols
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy import sin,cos,pi,exp
from sympy import simplify, expand, factor, trigsimp
x,y,z=symbols('x y z')

sol=solve(x**2+x+1/x+1/x**2-4,x)
print(sol)

e=0.8
M=9
E_sol=solveset(x-e*sin(x)-M)
print(E_sol)