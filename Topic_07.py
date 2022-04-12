"""
Тема 8: “Абстракция”
	•	Создать базовый абстрактный класс “Pair” (пара чисел) с арифметическими операциями:
сложение, вычитание, умножение и деление. Определить производный класс “Fuzzy numbers” (нечеткие числа),
реализующий арифметические операции следующим образом:
	•	A(A-a, A, A+a) + B(B-b, B, B+b) = ((A-a)+(B-b), A+B, (A+a)+(B+b))
	•	A(A-a, A, A+a) - B(B-b, B, B+b) = ((A-a)-(B-b), A-B, (A+a)-(B+b))
	•	A(A-a, A, A+a) * B(B-b, B, B+b) = ((A-a)*(B-b), A*B, (A+a)*(B+b))
	•	A(A-a, A, A+a) / B(B-b, B, B+b) = ((A-a)/(B-b), A/B, (A+a)/(B+b))
* решите самостоятельно, какими свойствами будет обладать каждый из классов, и какие методы следует определить как
абстрактные.
"""
from abc import ABC, abstractmethod

class Pair(ABC):
    def __init__(self, a, b):
        self.A = a
        self.B = b

    @abstractmethod
    def sum(self):
        pass

    @abstractmethod
    def minus(self):
        pass

    @abstractmethod
    def mult(self):
        pass

    @abstractmethod
    def div(self):
        pass

class Fuzzy_numbers(Pair):
    def __init__(self, a, A, b, B):
        super().__init__(A, B)
        self.a = a
        self.b = b

    def sum(self):
        l = ((self.A - self.a) + (self.B - self.b))
        c = self.A + self.B
        r = ((self.A + self.a) + (self.B + self.b))
        print(f'A: ({self.A - self.a}, {self.A}, {self.A + self.a}) + '
              f'B: ({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C: ({l}, {c}, {r})')
        return l, c, r

    def minus(self):
        l = ((self.A - self.a) - (self.B - self.b))
        c = self.A + self.B
        r = ((self.A + self.a) - (self.B + self.b))
        print(f'A: ({self.A - self.a}, {self.A}, {self.A + self.a}) - '
              f'B: ({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C: ({l}, {c}, {r})')
        return l, c, r

    def mult(self):
        l = ((self.A - self.a) * (self.B - self.b))
        c = self.A + self.B
        r = ((self.A + self.a) * (self.B + self.b))
        print(f'A: ({self.A - self.a}, {self.A}, {self.A + self.a}) * '
              f'B: ({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C: ({l}, {c}, {r})')
        return l, c, r

    def div(self):
        l = ((self.A - self.a) / (self.B - self.b))
        c = self.A + self.B
        r = ((self.A + self.a) / (self.B + self.b))
        print(f'A: ({self.A - self.a}, {self.A}, {self.A + self.a}) / '
              f'B: ({self.B - self.b}, {self.B}, {self.B + self.b}) = '
              f'C: ({l:.2f}, {c:.2f}, {r:.2f})')
        return l, c, r


fn = Fuzzy_numbers(5, 3, 10, 2)
fn.sum()
print()
fn.minus()
print()
fn.mult()
print()
fn.div()
print()
