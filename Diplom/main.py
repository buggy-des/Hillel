import tkinter as tk
from tkinter import messagebox, filedialog
from person import Person
from data import PersonData


class PersonApp:
    def __init__(self, root):
        self.db = PersonData()
        self.root = root
        self.root.title("Система обліку осіб")
        self.root.geometry("400x500")
        self.root.config(bg='#F6F4D4')
        self.root.iconphoto(False, tk.PhotoImage(file='icon.png'))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.greet_label = tk.Label(root, font=('Arial', 16, 'bold'), text='Вітаю!\nЩо будемо робити?', bg='#F6F4D4')
        self.greet_label.grid(row=0, column=0, pady=30, sticky='nsew')

        self.menu_frame = tk.Frame(self.root, bg='#F6F4D4')
        self.menu_frame.grid(row=1, column=0, sticky='nsew')

        self.menu_frame.grid_rowconfigure(0, weight=1)
        self.menu_frame.grid_rowconfigure(1, weight=1)
        self.menu_frame.grid_rowconfigure(2, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(1, weight=1)

        self.add_person_button = tk.Button(self.menu_frame, bd=5,
                                           text="Додати особу", command=self.add_person)
        self.add_person_button.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.view_people_button = tk.Button(self.menu_frame, bd=5,
                                            text="Відобразити всіх", command=self.view_people)
        self.view_people_button.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.search_person_button = tk.Button(self.menu_frame, bd=5,
                                              text="Пошук особи у базі", command=self.search_person)
        self.search_person_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        self.load_file_button = tk.Button(self.menu_frame, bd=5,
                                          text="Завантажити файл", command=self.load_file)
        self.load_file_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        self.save_file_button = tk.Button(self.menu_frame, bd=5,
                                          text="Зберегти дані у файл", command=self.save_file)
        self.save_file_button.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        self.exit_button = tk.Button(self.menu_frame, bd=5, text="Вихід", command=self.root.quit)
        self.exit_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    def add_person(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Додати особу")

        self.new_window.geometry("400x350")

        self.label_first_name = tk.Label(self.new_window, text="Введіть ім'я:")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(self.new_window)
        self.entry_first_name.pack()

        self.label_patronymic = tk.Label(self.new_window, text="Вкажіть по-батькові (необов'язково):")
        self.label_patronymic.pack()
        self.entry_patronymic = tk.Entry(self.new_window)
        self.entry_patronymic.pack()

        self.label_surname = tk.Label(self.new_window, text="Вкажіть прізвище (необов'язково):")
        self.label_surname.pack()
        self.entry_surname = tk.Entry(self.new_window)
        self.entry_surname.pack()

        self.label_gender = tk.Label(self.new_window, text="Яка стать?:")
        self.label_gender.pack()
        self.entry_gender = tk.Entry(self.new_window)
        self.entry_gender.pack()

        self.label_date_of_birth = tk.Label(self.new_window, text="Дата народження:")
        self.label_date_of_birth.pack()
        self.entry_date_of_birth = tk.Entry(self.new_window)
        self.entry_date_of_birth.pack()

        self.label_date_of_death = tk.Label(self.new_window, text="Дата смерті (якщо таке сталося):")
        self.label_date_of_death.pack()
        self.entry_date_of_death = tk.Entry(self.new_window)
        self.entry_date_of_death.pack()

        self.add_button = tk.Button(self.new_window, text="Додати", command=self.save_new_person)
        self.add_button.pack(pady=10)

    def save_new_person(self):
        first_name = self.entry_first_name.get().title()
        patronymic = self.entry_patronymic.get().title()
        surname = self.entry_surname.get().title()
        gender = self.entry_gender.get()
        date_of_birth = self.entry_date_of_birth.get()
        date_of_death = self.entry_date_of_death.get()

        try:
            person = Person(first_name, gender, date_of_birth, date_of_death, surname, patronymic)
            self.db.add_person(person)
            messagebox.showinfo("Успіх", f"Особу додано:\n {person.first_name}")
            self.new_window.destroy()
        except ValueError as e:
            messagebox.showerror("Помилка", str(e))

    def view_people(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Відобразити всіх")
        self.new_window.geometry('900x500')

        self.output_text = tk.Text(self.new_window, wrap="word", width=150, height=50)
        self.output_text.pack(pady=10)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, str(self.db))

    def search_person(self):
        self.search_window = tk.Toplevel(self.root)
        self.search_window.title("Пошук особи")
        self.search_window.geometry('250x100')

        self.label_search = tk.Label(self.search_window, text="Кого шукаємо?:")
        self.label_search.pack()
        self.entry_search = tk.Entry(self.search_window)
        self.entry_search.pack()

        self.search_button = tk.Button(self.search_window, text="Шукати", command=self.perform_search)
        self.search_button.pack(pady=10)

    def perform_search(self):
        request = self.entry_search.get()
        results = self.db.find_person(request)
        result_window = tk.Toplevel(self.root)
        result_window.geometry('900x500')
        result_window.title("Результати пошуку")

        self.output_text = tk.Text(result_window, wrap="word", width=150, height=50)
        self.output_text.pack(pady=10)
        if results:
            for result in results:
                self.output_text.insert(tk.END, result + "\n" + ('-' * 100 + '\n'))
        else:
            self.output_text.insert(tk.END, f"Людина {request} відсутня у базі.\n")

        self.search_window.destroy()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xlsm;*.xltx;*.xltm")])
        if file_path:
            try:
                self.db.load_from_file(file_path)
                messagebox.showinfo("Успіх", "Дані завантажено успішно.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx;*.xlsm;*.xltx;*.xltm")])
        if file_path:
            try:
                self.db.save_to_file(file_path)
                messagebox.showinfo("Успіх", "Дані збережено успішно.")
            except Exception as e:
                messagebox.showerror("Помилка", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = PersonApp(root)
    root.mainloop()
