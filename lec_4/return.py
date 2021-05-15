def my_func(a,b):
  ''' Функция которая считает что-то из запиханных в неё аргументов и возвращает их
  '''
  x1=3*a-2*b
  x2=5*a-4*b
  return x1, x2

tmp=my_func(3,2)

print(type(tmp))
