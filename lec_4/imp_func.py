from lec_4_m import *
tmp=mult_func(4)
print(tmp)
print(mult_func(10))
print(mult_func('Good'))
print_func('Hello')
print_func(mult_func('50'))

x0=10
def move(t):
  x=x0*t
  return x
print(move(3))
a='Good'
def my_func():
  a='Bad'
  print(a)
my_func()
print(a)