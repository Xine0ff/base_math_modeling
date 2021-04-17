import numpy as np
x0=0
y0=0
vx=1
vy=2
t=np.arange(0,5,0.1)
g=9.8
x=x0+vx*t
print(x)
y=y0+vx*t-(g*(t**2))/2
print(y)