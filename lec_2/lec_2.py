x=3
y=((x**(1/3))/(x**2-(3/x)))*(4*(x**8)+7*(x**4)+x**5)-80*((2*(x**5)+9*(x**3))**(1/2))
print(y)
y=(3%2+(16.7*4.32)//1)/((14.5+(32%12))-((x**3.4)//1))
print(y)
#уравнения

print(bool(0))
print(bool(''))
print(bool([]))
#бул

a=3
b=4
c=5
if a>4 and b==4:
  print(1)
if b>3 or c==5:
  print(2)
else:
  print(3)
#if

n=float(input('Введите число: '))
if n//2==n/2:
  print('Число четное')
else:
  print('Число нечетное')
#четное/нечетное

for i in 1,3,5:
  print(i**5, sep="\n")
a=[5,7,17,34]
for i in a:
  print(f'{i}**3={i**3}')
a='Good'
for i in range(0,10,1):
  if i<len(a):
    print(a[i]+' - Bad')
  else:
    print(f'{i} - Good')
#for

x=int(input('Введите сумму денег: '))
y=int(input('Введите процент: '))/100
n=int(input('Введите время (сколькое лет): '))
for i in range(0,n):
  x+=x*y
print(f'Итог: {x} денег')
#вклад (нет блин вкид)