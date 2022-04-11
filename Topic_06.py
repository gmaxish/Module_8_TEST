"""
	•	Внести изменения в созданный в первой задаче класс “Alcohol”: переопределить методы вычисления массы и объема
жидкости таким образом, чтобы в них также рассчитывалось соответственно массовое или объемное содержание чистого спирта,
исходя из заданной крепости.
Переопределить метод вывода информации о спирте.
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

    def v_liquid(self, m):
        v = super().v_liquid(m)
        v_alc = v * self.density
        print('+acl')
        return v, v_alc

    def m_liquid(self, v):
        m = super().v_liquid(v)
        m_alc = m * self.density
        print("++alc")
        return m, m_alc

    def print_info(self):
        return print(f'Liquid name is: {self.name}. It has {self.density} density and strenght {self.strenght}.')