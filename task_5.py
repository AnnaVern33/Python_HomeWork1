# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1 = float(input("Введите 1 координату для точки А: "))
y1 = float(input("Введите 2 координату для точки А: "))

x2 =float(input("Введите 1 координату для точки B: "))
y2 = float(input("Введите 1 координату для точки B: "))


distance = round(((x2 - x1)**2 + (y2 - y1)**2) **(0.5), 3)
print(distance)
