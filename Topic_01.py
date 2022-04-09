"""
Контрольная работа №5
Темы 1-4: “Классы и объекты. Свойства и методы класса. Конструктор, инициализатор, деструктор”

	•	Создать класс “Account”, представляющий собой банковский счет. Класс должен содержать:
	•	динамические свойства: фамилия владельца, номер счета, процент начисления, сумма в гривнах;
	•	статические свойства: курс гривны по отношению к доллару, курс гривны по отношению к евро;
	•	классовые методы: редактировать курс гривны по отношению к доллару, редактировать курс гривны по отношению к евро;
	•	статические методы: перевод суммы в доллары и евро;
	•	конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового банковского счета;
	•	инициализатор: определяет динамические свойства класса и выводит информацию об открытом счете;
	•	деструктор: выводит сообщение о том, что банковский счет закрыт;
	•	методы: смена владельца счета, снятие заданной суммы, начисление заданной суммы, начисление процентов, перевод
в доллары и евро (в отличие от аналогичных статических методов, данные методы не принимают параметров), вывод информации
о счете;
Продемонстрировать работу класса и всех его методов.
"""


class Account():
    rate_to_usd = 0.034
    rate_to_euro = 0.031
    suffix = "HRN"
    suffix_usd = "USD"
    suffix_euro = "EURO"

    def __new__(cls, *args, **kwargs):
        print("New account was created!")
        return super().__new__(cls)

    def __init__(self, surname, num, percent, amount=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.amount = amount
        print(f'The account #{self.num} owned by {self.surname} was opened.')

    def __del__(self):
        print("*" * 50)
        print(f'The account #{self.num} owned by {self.surname} was closed.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_to_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_to_euro = rate

    @staticmethod
    def convertation(value, rate):
        return value * rate

    def edit_owner(self, new_surname):
        self.surname = new_surname

    def print_balance(self):
        print(f'Your balance is {self.amount} {Account.suffix}')

    def withdraw_money(self, val):
        if val > self.amount:
            print(f'Unfortunately, you have not {val} {Account.suffix}')
        else:
            self.amount -= val
            print(f'{val} {Account.suffix} was withdrawed')

        self.print_balance()

    def add_money(self, value):
        self.amount += value
        print(f'{value} {Account.suffix} was added to your account')
        self.print_balance()

    def add_percent(self):
        self.amount += self.amount * self.percent
        print("The percents was added!")
        self.print_balance()

    def convert_to_usd(self):
        value_usd = Account.convertation(self.amount, Account.rate_to_usd)
        print(f'The currency balance in {Account.suffix_usd} is {value_usd}')

    def convert_to_euro(self):
        value_euro = Account.convertation(self.amount, Account.rate_to_euro)
        print(f'The currency balance in {Account.suffix_euro} is {value_euro}')

    def print_info(self):
        print("Account info:")
        print(f'#{self.num}')
        print(f'Owner is: {self.surname}')
        self.print_balance()
        print(f'Percent is {self.percent:.0%}')


acc = Account(surname="Hryhorovych", num="067573", percent=0.04, amount=1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_euro()
print()

Account.set_usd_rate(2)
Account.set_euro_rate(3)
acc.convert_to_usd()
acc.convert_to_euro()
print()

acc.edit_owner(new_surname="NeHryhorovych")
acc.print_info()
print()

acc.add_percent()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(1500)
print()

acc.add_money(5000)
print()

acc.withdraw_money(1500)
print()