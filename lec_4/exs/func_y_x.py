import math as m
import numpy as np
def s_func(a=0,b=99):
  x=np.linspace(a,b,100)
  y=x**2
  return y
print(s_func())