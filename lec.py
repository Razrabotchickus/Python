#Урок 1
#1.Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, является ли этот день выходным.
"""
print('Введите номер дня недели:')
day = int(input())
if day <= 7 and day >= 5:
    print ('Да')
else:
    print ('Нет')
"""
#1.Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
print('Введите предикат X:')
X = (input())
print('Введите предикат Y:')
Y = (input())
print('Введите предикат Z:')
Z = (input())
a = not (X or Y or Z) 
b = not X and not Y and not Z
result = a == b
#print (result)
"""
#2.Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).
"""
print('Введите координату X:')
X = int(input())
print('Введите координату Y:')
Y = int(input())
if X > 0 and Y > 0:
    print ("I четверть плоскости")
elif X < 0 and Y > 0:
    print ("II четверть плоскости")
elif X < 0 and Y < 0:
    print ("III четверть плоскости")
elif X > 0 and Y < 0:
    print ("IV четверть плоскости")
else:
    print("Вы ввели нулевые координаты X и Y.")
"""
#1Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).
"""
print('Введите номер плоскости(1-4):')
ploskost = int(input())
if ploskost == 1:
    print ("0:+∞ ; 0:+∞")
elif ploskost == 2:
    print ("0:-∞ ; 0:+∞")
elif ploskost == 3:
    print ("0:-∞ ; 0:-∞")
elif ploskost == 4:
    print ("0:+∞ ; 0:-∞")
else:
    print("Вводить нужно от 1 до 4")
"""
#Напишите программу, которая принимает на вход координаты двух точек
#и находит расстояние между ними в 2D пространстве.
print('Введите координаты первой точки:')
x1 = int(input())
y1 = int(input())
print('Введите координаты второй точки:')
x2 = int(input())
y2 = int(input())
dlina = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5),3)
print(dlina)