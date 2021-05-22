def st(a,n):
  if n>0:
    b=1
    for i in range(n):
      b=b*a
  elif n<0:
    if a==0:
      b='error'
    else:
      b=1
      n=-n
      for i in range(n):
        b=b/a
  else:
    b=1
  return b

print(st(2,-10))