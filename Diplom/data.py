import openpyxl
from person import Person


class PersonData:
    def __init__(self):
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def load_from_file(self, filename: str):
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        self.people = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            self.add_person(Person(*row))

    def find_person(self, request: str):
        request = request.lower().strip()
        return [person for person in self.people if request in person.first_name.lower() or
                request in (person.surname.lower() if person.surname else '') or
                request in (person.patronymic.lower() if person.patronymic else '')]

    def save_to_file(self, filename: str):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['ім\'я', 'По-батькові', 'Прізвище', 'Стать', 'Вік', 'Дата народження', 'Дата смерті'])
        for person in self.people:
            ws.append(person.person_info())
        wb.save(filename)

    def __str__(self):
        return '\n'.join(str(person) for person in self.people)
