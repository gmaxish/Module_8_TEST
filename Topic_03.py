"""
	•	Создать класс “Time” для работы со временем в формате Час:Минута:Секунда. Класс должен содержать:
	•	динамические свойства: количество часов, минут, секунд;
	•	статическое свойство: часовой пояс (строка в формате “UTC+/-число”);
	•	классовые методы: редактировать часовой пояс;
	•	статические методы: проверка корректности заданных величин (часов, минут, секунд), перевод заданного значения
из формата Час:Минута:Секунда в секунды и наоборот;
	•	конструктор: вызывает конструктор родительского класса и выводит сообщение о создании нового момента времени;
	•	инициализатор: проверяет корректность переданных величин, определяет динамические свойства класса и выводит на
экран информацию об объекте;
	•	деструктор: выводит сообщение о том, что момент времени удален;
	•	методы: вычисление разницы между двумя моментами времени в секундах, сложение с заданным количеством секунд,
вычитание заданного количества секунд, сравнение двух моментов времени, вывод на экран;
Продемонстрировать работу класса и всех его методов.
"""


class Time:
    pref = 'UTC'
    min_value_offset = -12
    max_value_offset = 14
    offset = 2
    timezone = '{pref}{offset:+}'.format(pref=pref, offset=offset)

    def __new__(cls, *args, **kwargs):
        print("New timestamp was created.")
        return super().__new__(cls)

    def __init__(self, hours, minutes, seconds):
        if Time.is_correct(hours, minutes, seconds):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

            self.print_info()
        else:
            print("Wrong data!")

    def __del__(self):
        print(f'The timestamp {self.get_str()} was deleted')

    @classmethod
    def edit_offset(cls, value):
        if cls.min_value_offset <= value <= cls.max_value_offset:
            cls.offset = value
        else:
            print(f'Wrong value! For {cls.pref} time offset should be '
                  f'from {cls.min_value_offset:+} to {cls.max_value_offset:+}')

    @staticmethod
    def is_correct(hours, minutes, seconds):
        return hours in range(0, 24) and minutes in range(0, 60) and seconds in range(0, 60)

    @staticmethod
    def convert_to_seconds(hours, minutes, seconds):
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def convert_from_seconds(seconds):
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        sec = seconds % 60
        return hours, minutes, sec

    def get_str(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def print_info(self):
        print(f'The timestamp: {self.hours:02}:{self.minutes:02}:{self.seconds:02}')

    def difference_in_seconds(self, timestamp):
        time1 = self.convert_to_seconds(self.hours, self.minutes, self.seconds)
        time2 = self.convert_to_seconds(timestamp.hours, timestamp.minutes, timestamp.seconds)
        result = time2 - time1
        print(f'The difference between {self.hours:02}:{self.minutes:02}:{self.seconds:02} and '
              f'{timestamp.hours:02}:{timestamp.minutes:02}:{timestamp.seconds:02} is {result:+} seconds.')

    def plus_seconds(self, seconds):
        time1 = self.convert_to_seconds(self.hours, self.minutes, self.seconds)
        time1 += seconds
        self.hours, self.minutes, self.seconds = Time.convert_from_seconds(time1)
        self.print_info()

    def minus_seconds(self, seconds):
        time1 = self.convert_to_seconds(self.hours, self.minutes, self.seconds)
        time1 -= seconds
        self.hours, self.minutes, self.seconds = Time.convert_from_seconds(time1)
        self.print_info()

    def is_the_same_moment(self, timestamp):
        res = self.hours == timestamp.hours and self.minutes == timestamp.minutes and self. seconds == timestamp.seconds
        print(f'The times {self.hours:02}:{self.minutes:02}:{self.seconds:02} and '
              f'{timestamp.hours:02}:{timestamp.minutes:02}:{timestamp.seconds:02} '
              f'are {"not" if not res else ""} the same')
        return res


t1 = Time(26, 12, 5)
t2 = Time(22, 70, 30)
t3 = Time(14, 21, 62)
t4 = Time(14, 21, 12)
print()