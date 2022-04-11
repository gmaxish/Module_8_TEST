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
            self.set_hours(hours)
            self.set_minutes(minutes)
            self.set_seconds(seconds)

            self.print_info()
        else:
            self.set_hours(0)
            self.set_minutes(0)
            self.set_seconds(0)

            print("Wrong data!")

    def __del__(self):
        print(f'The timestamp {self.get_str()} was deleted')

    def set_hours(self, hours):
        self._hours = hours

    def get_hours(self):
        return self._hours

    def set_minutes(self, minutes):
        self._minutes = minutes

    def get_minutes(self):
        return self._minutes

    def set_seconds(self, seconds):
        self._seconds = seconds

    def get_seconds(self):
        return self._seconds

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
        return f'{self.get_hours():02}:{self.get_minutes():02}:{self.get_seconds():02}'

    def print_info(self):
        print(f'The timestamp: {self.get_hours():02}:{self.get_minutes():02}:{self.get_seconds():02}')

    def difference_in_seconds(self, timestamp):
        time1 = self.convert_to_seconds(self.get_hours(), self.get_minutes(), self.get_seconds())
        time2 = self.convert_to_seconds(timestamp.get_hours(), timestamp.get_minutes(), timestamp.get_seconds())
        result = time2 - time1
        print(f'The difference between {self.get_hours():02}:{self.get_minutes():02}:{self.get_seconds():02} and '
              f'{timestamp.get_hours():02}:{timestamp.get_minutes():02}:{timestamp.get_seconds():02} is {result:+} '
              f'seconds.')

    def plus_seconds(self, seconds):
        time1 = self.convert_to_seconds(self.get_hours(), self.get_minutes(), self.get_seconds())
        time1 += seconds
        hours, minutes, seconds = Time.convert_from_seconds(time1)
        self.set_hours(hours)
        self.set_minutes(minutes)
        self.set_seconds(seconds)
        self.print_info()

    def minus_seconds(self, seconds):
        time1 = self.convert_to_seconds(self.get_hours(), self.get_minutes(), self.get_seconds())
        time1 -= seconds
        hours, minutes, seconds = Time.convert_from_seconds(time1)
        self.set_hours(hours)
        self.set_minutes(minutes)
        self.set_seconds(seconds)
        self.print_info()

    def is_the_same_moment(self, timestamp):
        res = self.get_hours() == timestamp.get_hours() and self.get_minutes() == timestamp.get_minutes()\
              and self. get_seconds() == timestamp.get_seconds()
        print(f'The times {self.get_str()} and '
              f'{timestamp.hours:02}:{timestamp.minutes:02}:{timestamp.seconds:02} '
              f'are {"not" if not res else ""} the same')
        return res


t1 = Time(26, 12, 5)
t2 = Time(22, 70, 30)
t3 = Time(14, 21, 62)
t4 = Time(14, 21, 12)
print()

Time.edit_offset(10)
print(Time.offset)