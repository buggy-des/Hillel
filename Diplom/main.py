from person import Person
from data import PersonData


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
        choice = input("Оберіть з меню (1-6): ")

        if choice == '1':
            first_name = input("Введіть ім'я: ")
            patronymic = input("Вкажіть по-батькові (необов'язково): ")
            surname = input("Вкажіть прізвище (необов'язково): ")
            gender = input("Яка стать?: ")
            date_of_birth = input("Дата народження: ")
            date_of_death = input("Дата смерті (якщо таке сталося): ")
            person = Person(first_name, gender, date_of_birth, date_of_death, surname, patronymic)
            db.add_person(person)
        elif choice == '2':
            print(db) if db else print("База даних порожня")
        elif choice == '3':
            request = input("Кого шукаємо?: ")
            results = db.find_person(request)
            for result in results:
                print(result)
        elif choice == '4':
            filename = input("Назва файлу для завантаження: ")
            db.load_from_file(filename)
        elif choice == '5':
            filename = input("Назва файлу для збереження: ")
            db.save_to_file(filename)
        elif choice == '6':
            print("Дякую за роботу.\nБережіть себе!")
            break
        else:
            print("Невірний вибір!\nПовторіть введення.")


if __name__ == '__main__':
    main()
