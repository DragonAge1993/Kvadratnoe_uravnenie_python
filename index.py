#http://rtfm.co.ua/python_s_nulya/python-s-nulya-chast-2-tipy-peremennyx/
import math
__author__ = 'anonymousblack'
print("Доброго времени суток, вас приветствует программа подсчета квадратного уравнения")
a = input("Введите значение А: ")
a1 = int(a , 0)#преобразование строки a в целое
print(a1)
b = input("Введите значение B: ")
b1 = int(b , 0)#преобразование строки b в целое
print(b1)
c = input("Введите значение C: ")
c1 = int(c , 0)#преобразование строки c в целое
print(c1)
D = pow(b1,2) - 4*a1*c1 # pow - вводим в степень
if D<0: #Нет корней
    print("Корней нет")
if D>0: # Два корня
    print("Два корня:)")
    x1 = (-b1 + math.sqrt(D))/(2*a1)
    x2 = (-b1 - math.sqrt(D))/(2*a1)
    print(x1)
    print(x2)
else: # Если D=0, то один корень
    print("Один корень ")
    x = (-b1/(2*a1))
    print(x)