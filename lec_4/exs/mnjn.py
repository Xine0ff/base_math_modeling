import numpy as np
def mnjn(x):
  e=1
  for i in range(0,len(x),1):
    e=e*x[i]
  return e
print(mnjn(np.linspace(1,100,10)))
print(np.linspace(1,10,10))