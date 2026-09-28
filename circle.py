import math


def area(r):
    '''
    Принимает радиус круга r и возвращает площадь круга.
    Пример вызова: area(5)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус круга r и возвращает длину окружности.
    Пример вызова: perimeter(5)
    '''
    return 2 * math.pi * r