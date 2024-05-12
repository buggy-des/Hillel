import time
from person import Person
from data import PersonData


def is_not_empty(func):
    def wrapper(*args, required=True, **kwargs):
        while True:
            result = func(*args, **kwargs)
            if result.strip() or not required:
                return result
            print("Введення не може бути порожнім. Спробуйте ще раз.")
            if not required:
                return None
    return wrapper


@is_not_empty
def valid_input(text):
    return input(text)


def main():
    db = PersonData()
    while True:
        print("Меню:")
        print("1. Додати особу")
        print("2. Відобразити всіх")
        print("3. Пошук особи у базі")
        print("4. Завантажити файл")
        print("5. Зберегти дані у файл")
        print("6. Вихід")
        choice = valid_input("Оберіть з меню (1-6): ")

        if choice == '1':
            first_name = valid_input("Введіть ім'я: ").title()
            patronymic = valid_input("Вкажіть по-батькові (необов'язково): ", required=False).title()
            surname = valid_input("Вкажіть прізвище (необов'язково): ", required=False).title()
            gender = valid_input("Яка стать?: ")
            date_of_birth = valid_input("Дата народження: ")
            date_of_death = valid_input("Дата смерті (якщо таке сталося): ", required=False)
            person = Person(first_name, gender, date_of_birth, date_of_death, surname, patronymic)
            db.add_person(person)
            print(f"Додано {person}")
        elif choice == '2':
            print(db)
        elif choice == '3':
            request = valid_input("Кого шукаємо?: ")
            results = db.find_person(request)
            for result in results:
                print(result)
        elif choice == '4':
            filename = valid_input("Назва файлу для завантаження: ")
            db.load_from_file(filename)
            time.sleep(1)
        elif choice == '5':
            filename = valid_input("Назва файлу для збереження"
                                   "\nОбов'язково додайте розширення (.xlsx,.xlsm,.xltx,.xltm): ")
            db.save_to_file(filename)
            time.sleep(1)
        elif choice == '6':
            print("Завершення програми...")
            time.sleep(1)
            print("Дякую за роботу.\nБережіть себе!")
            break
        else:
            print("Невірний вибір!\nПовторіть введення.")


if __name__ == '__main__':
    main()
