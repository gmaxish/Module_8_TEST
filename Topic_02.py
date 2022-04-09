"""
	•	Создать класс “Point” для работы с точками на плоскости. Класс должен содержать:
	•	динамические свойства: координаты точки X и Y;
	•	статические свойства: количество точек, лежащих на оси X, количество точек, лежащих на оси Y, количество точек,
совпадающих с началом координат;
	•	классовые методы: увеличить на 1 количество точек, лежащих на оси X, увеличить на 1 количество точек, лежащих
на оси Y, увеличить на 1 количество точек, совпадающих с началом координат;
	•	статические методы: проверки, лежит ли точка на одной из осей координат или совпадает с началом координат;
	•	конструктор: вызывает конструктор родительского класса и выводит сообщение о создании новой точки;
	•	инициализатор: определяет динамические свойства класса и выводит созданный объект на экран;
	•	деструктор: выводит сообщение о том, что точка удалена;
	•	методы: перемещение точки по оси X, перемещение точки по оси Y, определение расстояния до начала координат,
вычисление расстояния до заданной точки, сравнение на совпадение и несовпадение с заданной точкой, вывод точки на экран;
* заданная точка - также экземпляр класса “Point”.
Продемонстрировать работу класса и всех его методов.
"""

class Point():
    ox_count = 0
    oy_count = 0
    oo_count = 0

    def __new__(cls, *args, **kwargs):
        print("New point was created!")
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("-" * 30)
        print(f' The point is: {self.x} {self.y}')
        print("-" * 30)

    def __del__(self):
        print(f'The point {self.x} {self.y} was deleted.')

    @classmethod
    def inc_ox_count(cls):
        cls.ox_count += 1

    @classmethod
    def inc_oy_count(cls):
        cls.oy_count += 1

    @classmethod
    def inc_oo_count(cls):
        cls.oo_count += 1

    @staticmethod
    def is_start_point(x, y):
        return x == 0 and y == 0

    @staticmethod
    def point_on_ox(y):
        return y == 0

    @staticmethod
    def point_on_oy(x):
        return x == 0

    def move_ox(self, x):
        self.x += x

    def move_oy(self, y):
        self.y += y

