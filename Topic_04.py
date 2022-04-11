"""
Темы 6-7: “Наследование. Множественное наследование. Полиморфизм”
	•	Создать класс “Liquid” (жидкость) со свойствами: название и плотность жидкости, - и методами: изменение
плотности, вычисление объема жидкости, соответствующего заданной массе, вычисление массы жидкости, соответствующей
заданному объему, вывод информации о жидкости.
Создать производный класс “Alcohol” (спирт) с собственным свойством -крепость, - и методом: изменение крепости.
Продемонстрировать работу класса-наследника и всех его методов.
"""

class Liquid:

    def __init__(self, name, density):
        self.name = name
        self.density = density

    def change_density(self, val):
        self.density = val

    def v_liquid(self, m):
        v = round(m / self.density, 2)
        print(f'The volume of {m} kg of {self.name} is {v} kg^3.')
        return v

    def m_liquid(self, v):
        m = v * self.density
        print(f'The weight of {v:.2f} m^3 of {self.name} is {m:.2f} kg.')
        return m

    def print_info(self):
        return print(f'Liquid name is: {self.name}. It has {self.density} density.')

class Alcohol(Liquid):
    def __init__(self, name, density, strenght):
        super().__init__(name, density)
        self.strenght = strenght

    def change_strenght(self, val):
        self.strenght = val


a = Alcohol("Vine", 1060.1, 4)
a.print_info()

a.change_density(12)
a.print_info()
a.v_liquid(10)
a.m_liquid(12)
a.change_strenght(13)
a.print_info()