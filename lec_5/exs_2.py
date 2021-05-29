import sympy
from sympy import symbols
from sympy import simplify, expand, factor, trigsimp
x,y,z=symbols('x y z')
expr1=simplify((x*y**2-2*x*y*z+x*y**2+y**2-2*y*z+z**2)/(x**2-1))
print(expr1)
a=1
expr2=simplify( sympy.sqrt((1+sin(a))/(1-sin(a))) + sympy.sqrt((1-sin(a))/(1+sin(a))))
print(expr2)