import numpy as np
a=[1,2,4]
b=np.array(a)
print(type(a))
print(type(b))
print(b*b)
print(b/b)
print(b-b)
print(b[-1])
#

a=np.zeros((2,3))
print(a)
a[0,2]=5
print(a)
b=np.ones((3,2))
print(b)
d=np.ndarray((3,3))
print(d)
#рандом типа?

a=range(0,5,1)
print(a)
b=np.arange(0,5,0.1)
print(b)
d=np.linspace(0,5,10)
print(d)
#

a=[4,16,10,5,7,1,8]
slice=a[2:5:1]
print(slice)
#срезы

a='Mel lox, Hleb pyphon'
print(a[:3])
#срезы

a=[1,5,3,6]
slice=a[0:2:1]
print(slice)
slice=a[3:0:-1]
print(slice)
slice=a[::-1]
print(slice)
b=np.array([a,np.array(a)*3])
print(b)
#все еще срезы

slice=b[::,1]
print(slice)
slice=b[1,2:3:1]
print(slice)
slice=b[1,2::1]
print(slice)
#