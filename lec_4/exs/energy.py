g=9.8
def En(m,h,v):
  ek=(m*(v**2))/2
  ep=m*g*h
  E=ek+ep
  return E
print(En(2,2,4))