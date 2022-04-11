"""
Создать класс “Pair” (пара чисел) со свойствами: числа A и B, - и методами: изменение чисел, вычисление их произведения
и суммы. Определить производный класс “Right Triangle” (прямоугольный треугольник) со свойствами: катеты A и B, -
и методами: вычисление гипотенузы и площади треугольника, вывод информации о фигуре на экран.
Продемонстрировать работу класса-наследника и всех его методов.
"""
from  math import sqrt

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change_a(self, val):
        self.a = val

    def change_b(self, val):
        self.b = val

    def mult(self):
        return self.a * self.b

    def plus(self):
        return self.a + self.b


class Right_Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypot(self):
        hypot = round(sqrt((self.a ** 2) + (self.b ** 2)), 2)
        print(f'The hypotenuse of \u25B3ABC: {hypot}')
        return hypot

    def square(self):
        s = round(0.5 * self.mult(), 2)
        print(f'The square of \u25B3ABC: {s}')
        return s

    def print_info(self):
        print(f'The right triangle \u25B3ABC: {self.a}, {self.b}, {self.hypot()}')

tr = Right_Triangle(4, 4)
tr.print_info()
tr.change_a(5)
tr.print_info()