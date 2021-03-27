print(type(3))
print(type(1.5))
print(type('строка'))
print(type(['строка', 1, 'еще строка', 4.5, 9]))
print(type(True))
# типы данных

a=float(input('Введите значение a: '))
print(a)
print(type(a))
# ввод данных

a='Good'
b='Bad'
print(a+b)
print(a*3)
# сложение и умножение строк

c=1
d=2
print(f'Вставим числа {c} и {d}')
#f-строки

name=input('Как тебя зовут? ')
y=int(input(f'Привет, {name}! \nСколько тебе лет? '))
print(f'До 100 лет тебе осталось прожить {100-y} лет')
# комментарий

a=[1,2,3] 
print(a[0]) #1-ый элемент
print(a[-1]) #последний (3-ий) элемент
print(a[0]+a[-1])
b=[1,4,5]
c=a+b
print(c)
print(c*2)
s=[]
s.append(10)
print(s)
print(len(a)-1)
# список