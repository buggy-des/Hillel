import datetime


class Person:
    def __init__(self, first_name: str, gender: str, date_of_birth: str,
                 date_of_death: str = None, surname: str = None, patronymic: str = None):
        self.first_name = first_name
        self.surname = surname if surname else None
        self.patronymic = patronymic if patronymic else None
        self.gender = self.gender_value(gender)
        self.date_of_birth = self.date_format(date_of_birth)
        self.date_of_death = self.date_format(date_of_death) if date_of_death else None

    def gender_value(self, i):
        if i.lower().startswith(('m', 'м', 'ч')):
            return 'man'
        elif i.lower().startswith(('w', 'ж')):
            return 'woman'
        else:
            return '-'

    def date_format(self, date_str: str):
        if not date_str:
            return None
        for frmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%d %m %Y"):
            try:
                return datetime.datetime.strptime(date_str, frmt)
            except ValueError:
                continue
        raise ValueError(f"Невiрний формат дати {date_str}")

    def full_years(self):
        if not self.date_of_birth:
            raise ValueError("Дата народження обов'язкова для введення!")
        death_or_now = self.date_of_death or datetime.datetime.now().date()
        age = death_or_now.year - self.date_of_birth.year
        if (death_or_now.month, death_or_now.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def person_info(self):
        return [self.first_name,
                self.patronymic if self.patronymic else '-',
                self.surname if self.surname else '-',
                self.gender,
                self.full_years(),
                self.date_of_birth.strftime("%d.%m.%Y"),
                self.date_of_death.strftime("%d.%m.%Y") if self.date_of_death else '-'
                ]

    def __str__(self):
        info = self.person_info()
        formatted_info = [
            str(field).center(12) for field in info
        ]
        return ' | '.join(formatted_info)
