a=500
print(id(a))
a=a+5
print(id(a))

b=[500]
print(id(b))
b[0]=505
print(id(b))