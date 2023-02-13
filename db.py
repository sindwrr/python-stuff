from tkinter import *
from tkinter import messagebox
import psycopg2 as ps
from functools import partial

DB_NAME = "library"
DB_USER = "postgres"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5432"


class MainApp(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.chose_f = Frame(self)

        a_action_with_arg = partial(self.click_callback, 'admin')
        a_button = Button(self.chose_f, text='Администратор БД',
                          command=a_action_with_arg)
        a_button.pack(side=TOP, fill=BOTH, expand=1)

        r_action_with_arg = partial(self.click_callback, 'reg')
        r_button = Button(self.chose_f, text='Работник отдела записи',
                          command=r_action_with_arg)
        r_button.pack(side=TOP, fill=BOTH, expand=1)

        h_action_with_arg = partial(self.click_callback, 'hall')
        h_button = Button(self.chose_f, text='Работник читального зала',
                          command=h_action_with_arg)
        h_button.pack(side=TOP, fill=BOTH, expand=1)

        self.chose_f.pack(side=TOP, fill=BOTH, expand=1, anchor=CENTER)

    def empty(self):
        messagebox.showinfo("Info", "Пустое окно")

    def reader_list(self):
        conn = ps.connect(database=DB_NAME,
                          user=DB_USER,
                          password=DB_PASS,
                          host=DB_HOST,
                          port=DB_PORT)
        cur = conn.cursor()
        cur.execute("SELECT * FROM reader;")
        f = cur.fetchall()

        new_window = Toplevel(self)
        new_window.title("Читатели")
        new_window.geometry("600x300")
        Label(new_window, text="Номер чит. билета").grid(row=0, column=0)
        Label(new_window, text="Читальный зал").grid(row=0, column=1)
        Label(new_window, text="Фамилия").grid(row=0, column=2)
        Label(new_window, text="Номер телефона").grid(row=0, column=3)
        Label(new_window, text="Дата записи").grid(row=0, column=4)
        for i in range(len(f)):
            for j in range(len(f[i])):
                Label(new_window, text=f[i][j]).grid(row=i+1, column=j)
        conn.close()

    def book_list(self):
        conn = ps.connect(database=DB_NAME,
                          user=DB_USER,
                          password=DB_PASS,
                          host=DB_HOST,
                          port=DB_PORT)
        cur = conn.cursor()
        cur.execute("SELECT * FROM book;")
        f = cur.fetchall()

        new_window = Toplevel(self)
        new_window.title("Книги")
        new_window.geometry("600x300")

        Label(new_window, text="ID книги").grid(row=0, column=0)
        Label(new_window, text="Название").grid(row=0, column=1)
        Label(new_window, text="Автор").grid(row=0, column=2)
        Label(new_window, text="Год издания").grid(row=0, column=3)
        Label(new_window, text="Шифр").grid(row=0, column=4)
        for i in range(len(f)):
            for j in range(len(f[i])):
                Label(new_window, text=f[i][j]).grid(row=i+1, column=j)
        conn.close()

    def hall_list(self):
        conn = ps.connect(database=DB_NAME,
                          user=DB_USER,
                          password=DB_PASS,
                          host=DB_HOST,
                          port=DB_PORT)
        cur = conn.cursor()
        cur.execute("SELECT * FROM read_hall;")
        f = cur.fetchall()

        new_window = Toplevel(self)
        new_window.title("Читальные залы")
        new_window.geometry("400x200")
        Label(new_window, text="Номер зала").grid(row=0, column=0)
        Label(new_window, text="Название").grid(row=0, column=1)
        Label(new_window, text="Вместимость").grid(row=0, column=2)
        for i in range(len(f)):
            for j in range(len(f[i])):
                Label(new_window, text=f[i][j]).grid(row=i+1, column=j)
        conn.close()

    def add_reader(self):
        def submit():
            hall = hall_var.get()
            name = name_var.get()
            phone = phone_var.get()
            regdate = regdate_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""INSERT INTO reader (hall_id, last_name, phone_num, reg_date)
                            VALUES({hall}, '{name}', {phone}, '{regdate}');""")
                conn.commit()
                messagebox.showinfo("Info", "Данные успешно записаны!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Добавление читателя")
        new_window.geometry("300x200")

        hall_var = StringVar()
        name_var = StringVar()
        phone_var = StringVar()
        regdate_var = StringVar()

        Label(new_window, text='Номер зала').grid(row=0, column=0)
        Entry(new_window, textvariable=hall_var).grid(row=0, column=1)

        Label(new_window, text='Фамилия').grid(row=1, column=0)
        Entry(new_window, textvariable=name_var).grid(row=1, column=1)

        Label(new_window, text='Телефон').grid(row=2, column=0)
        Entry(new_window, textvariable=phone_var).grid(row=2, column=1)

        Label(new_window, text='Дата записи').grid(row=3, column=0)
        Entry(new_window, textvariable=regdate_var).grid(row=3, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=4, column=1)

    def delete_reader(self):
        def submit():
            id = id_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"DELETE FROM reader WHERE id = {id}")
                conn.commit()
                messagebox.showinfo("Info", "Данные успешно удалены!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Удаление читателя")
        new_window.geometry("300x200")

        id_var = StringVar()

        Label(new_window, text='Номер чит. билета').grid(row=0, column=0)
        Entry(new_window, textvariable=id_var).grid(row=0, column=1)
        Button(new_window, text='Ввести', command=submit).grid(row=1, column=1)

    def add_book(self):
        def submit():
            name = name_var.get()
            author = author_var.get()
            pyear = pyear_var.get()
            cipher = cipher_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""INSERT INTO book (book_name, author, pub_year, cipher)
                            VALUES('{name}', '{author}', {pyear}, '{cipher}');""")
                conn.commit()
                messagebox.showinfo("Info", "Данные успешно записаны!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Добавление книги")
        new_window.geometry("300x200")

        name_var = StringVar()
        author_var = StringVar()
        pyear_var = StringVar()
        cipher_var = StringVar()

        Label(new_window, text='Название').grid(row=0, column=0)
        Entry(new_window, textvariable=name_var).grid(row=0, column=1)

        Label(new_window, text='Автор').grid(row=1, column=0)
        Entry(new_window, textvariable=author_var).grid(row=1, column=1)

        Label(new_window, text='Год издания').grid(row=2, column=0)
        Entry(new_window, textvariable=pyear_var).grid(row=2, column=1)

        Label(new_window, text='Шифр').grid(row=3, column=0)
        Entry(new_window, textvariable=cipher_var).grid(row=3, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=4, column=1)

    def delete_book(self):
        def submit():
            id = id_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"DELETE FROM book WHERE id = {id}")
                conn.commit()
                messagebox.showinfo("Info", "Данные успешно удалены!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Удаление книги")
        new_window.geometry("300x200")

        id_var = StringVar()

        Label(new_window, text='ID книги').grid(row=0, column=0)
        Entry(new_window, textvariable=id_var).grid(row=0, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=1, column=1)

    def fix_book(self):
        def submit():
            reader = reader_var.get()
            book = book_var.get()
            date = date_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""INSERT INTO fixed_books
                            VALUES({reader}, {book}, '{date}');""")
                conn.commit()
                messagebox.showinfo("Info", "Книга успешно закреплена!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Закрепление книги")
        new_window.geometry("300x200")

        reader_var = StringVar()
        book_var = StringVar()
        date_var = StringVar()

        Label(new_window, text='Номер чит. билета').grid(row=0, column=0)
        Entry(new_window, textvariable=reader_var).grid(row=0, column=1)

        Label(new_window, text='ID книги').grid(row=1, column=0)
        Entry(new_window, textvariable=book_var).grid(row=1, column=1)

        Label(new_window, text='Дата закрепления').grid(row=2, column=0)
        Entry(new_window, textvariable=date_var).grid(row=2, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=3, column=1)

    def unfix_book(self):
        def submit():
            reader = reader_var.get()
            book = book_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""DELETE FROM fixed_books WHERE 
                            reader_id = {reader} AND book_id = {book};""")
                conn.commit()
                messagebox.showinfo("Info", "Книга успешно откреплена!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Открепление книги")
        new_window.geometry("300x200")

        reader_var = StringVar()
        book_var = StringVar()

        Label(new_window, text='Номер чит. билета').grid(row=0, column=0)
        Entry(new_window, textvariable=reader_var).grid(row=0, column=1)

        Label(new_window, text='ID книги').grid(row=1, column=0)
        Entry(new_window, textvariable=book_var).grid(row=1, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=2, column=1)

    def change_cipher(self):
        def submit():
            id = id_var.get()
            new_cipher = new_cipher_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(
                    f"UPDATE book SET cipher = '{new_cipher}' WHERE id = {id}")
                conn.commit()
                messagebox.showinfo("Info", "Шифр успешно изменён!")
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Изменение шифра книги")
        new_window.geometry("300x200")

        id_var = StringVar()
        new_cipher_var = StringVar()

        Label(new_window, text='ID книги').grid(row=0, column=0)
        Entry(new_window, textvariable=id_var).grid(row=0, column=1)

        Label(new_window, text='Новый шифр').grid(row=1, column=0)
        Entry(new_window, textvariable=new_cipher_var).grid(row=1, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=2, column=1)

    def books_fixed_to_reader(self):
        def submit():
            id = id_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""SELECT book.book_name, book.author FROM 
                fixed_books INNER JOIN book ON fixed_books.book_id = book.id 
                WHERE fixed_books.reader_id = {id};""")
                f = cur.fetchall()
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")
                Label(new_new_window, text="Название").grid(row=0, column=0)
                Label(new_new_window, text="Автор").grid(row=0, column=1)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+1, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Какие книги закреплены за читателем")
        new_window.geometry("300x200")

        id_var = StringVar()

        Label(new_window, text='Номер чит. билета').grid(row=0, column=0)
        Entry(new_window, textvariable=id_var).grid(row=0, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=1, column=1)

    def book_name_by_author(self):
        def submit():
            name = name_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(
                    f"SELECT book_name FROM book WHERE author = '{name}';")
                f = cur.fetchall()
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")
                Label(new_new_window, text="Название").grid(row=0, column=0)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+1, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Как называется книга с заданным автором")
        new_window.geometry("300x200")

        name_var = StringVar()

        Label(new_window, text='Фамилия И.О. автора').grid(row=0, column=0)
        Entry(new_window, textvariable=name_var).grid(row=0, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=1, column=1)

    def cipher_by_book_name(self):
        def submit():
            name = name_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(
                    f"SELECT cipher FROM book WHERE book_name = '{name}';")
                f = cur.fetchall()
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")
                Label(new_new_window, text="Шифр").grid(row=0, column=0)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+1, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Какой шифр у книги с заданным названием")
        new_window.geometry("300x200")

        name_var = StringVar()

        Label(new_window, text='Название').grid(row=0, column=0)
        Entry(new_window, textvariable=name_var).grid(row=0, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=1, column=1)

    def fixation_date(self):
        def submit():
            reader = reader_var.get()
            book = book_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""SELECT fix_date FROM fixed_books 
                WHERE reader_id = {reader} AND book_id = {book};""")
                f = cur.fetchall()
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")
                Label(new_new_window, text="Дата закрепления").grid(
                    row=0, column=0)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+1, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Когда книга была закреплена за читателем")
        new_window.geometry("300x200")

        reader_var = StringVar()
        book_var = StringVar()

        Label(new_window, text='Номер чит. билета').grid(row=0, column=0)
        Entry(new_window, textvariable=reader_var).grid(row=0, column=1)

        Label(new_window, text='ID книги').grid(row=1, column=0)
        Entry(new_window, textvariable=book_var).grid(row=1, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=2, column=1)

    def readers_num(self):
        conn = ps.connect(database=DB_NAME,
                          user=DB_USER,
                          password=DB_PASS,
                          host=DB_HOST,
                          port=DB_PORT)
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT(id) AS readers_num FROM reader;")
            f = cur.fetchall()
            messagebox.showinfo(
                "Info", f"Кол-во читателей на данный момент: {f[0][0]}")
        except:
            messagebox.showinfo("Info", "Ошибка. Проверьте данные")
        cur.close()
        conn.close()

    def copies_by_author(self):
        def submit():
            author = author_var.get()
            hall = hall_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                cur.execute(f"""SELECT book.book_name, copies.copies_num FROM 
                            book INNER JOIN copies ON book.id = copies.book_id 
                            WHERE book.author = '{author}' AND 
                            copies.hall_id = {hall};""")
                f = cur.fetchall()
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")
                Label(new_new_window, text="Книга").grid(
                    row=0, column=0)
                Label(new_new_window, text="Кол-во экзмепляров").grid(
                    row=0, column=1)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+1, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Наличие книг автора в читальном зале")
        new_window.geometry("300x200")

        author_var = StringVar()
        hall_var = StringVar()

        Label(new_window, text='Фамилия И.О. автора').grid(row=0, column=0)
        Entry(new_window, textvariable=author_var).grid(row=0, column=1)

        Label(new_window, text='Номер зала').grid(row=1, column=0)
        Entry(new_window, textvariable=hall_var).grid(row=1, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=2, column=1)

    def month_report(self):
        def submit():
            month = month_var.get()
            year = year_var.get()

            conn = ps.connect(database=DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
            cur = conn.cursor()
            try:
                new_new_window = Toplevel(new_window)
                new_new_window.title("Результат")
                new_new_window.geometry("600x400")

                cur.execute("SELECT COUNT(id) AS readers_num FROM reader;")
                f = cur.fetchall()
                Label(new_new_window, text="Общее кол-во читателей:").grid(
                    row=0, column=0)
                Label(new_new_window, text=f"{f[0][0]}").grid(
                    row=0, column=1)

                cur.execute(f"""SELECT COUNT(id) FROM reader 
                WHERE EXTRACT(MONTH FROM reg_date) = {month} 
                AND EXTRACT(YEAR FROM reg_date) = {year};""")
                f = cur.fetchall()

                Label(new_new_window, text=f"Кол-во читателей, записавшихся {month}.{year}:").grid(
                    row=1, column=0)
                Label(new_new_window, text=f"{f[0][0]}").grid(
                    row=1, column=1)

                cur.execute(f"""SELECT book.book_name, book.author, COUNT(book.book_name) FROM  
                            book INNER JOIN fixed_books ON book.id = fixed_books.book_id 
                            WHERE EXTRACT(MONTH FROM fixed_books.fix_date) = {month}
                            AND EXTRACT(YEAR FROM fixed_books.fix_date) = {year} 
                            GROUP BY book.book_name, book.author;""")
                f = cur.fetchall()

                Label(new_new_window, text="------------").grid(
                    row=2, column=0)
                Label(new_new_window, text=f"Какие книги сколько раз были взяты:").grid(
                    row=3, column=0)
                Label(new_new_window, text=f"Название").grid(
                    row=4, column=0)
                Label(new_new_window, text=f"Автор").grid(
                    row=4, column=1)
                Label(new_new_window, text=f"Кол-во закреплений").grid(
                    row=4, column=2)
                for i in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=i+5, column=j)

                cur.execute(f"""SELECT reader.last_name, reader.phone_num FROM 
                            fixed_books RIGHT JOIN reader ON fixed_books.reader_id = reader.id 
                            WHERE fixed_books.book_id = NULL  
                            OR (EXTRACT(MONTH FROM fixed_books.fix_date) != {month} 
                            AND EXTRACT(YEAR FROM fixed_books.fix_date) != {year});""")
                f = cur.fetchall()

                Label(new_new_window, text="------------").grid(
                    row=4+i+1+1, column=0)
                Label(new_new_window, text=f"Кто из читателей не брал книг за месяц:").grid(
                    row=4+i+2+1, column=0)
                Label(new_new_window, text=f"Фамилия").grid(
                    row=4+i+2+2, column=0)
                Label(new_new_window, text=f"Телефон").grid(
                    row=4+i+2+2, column=1)
                for k in range(len(f)):
                    for j in range(len(f[i])):
                        Label(new_new_window, text=f[i][j]).grid(
                            row=4+i+2+2+k, column=j)
            except:
                messagebox.showinfo("Info", "Ошибка. Проверьте данные")
            cur.close()
            conn.close()

        new_window = Toplevel(self)
        new_window.title("Отчет за месяц")
        new_window.geometry("300x200")

        month_var = StringVar()
        year_var = StringVar()

        Label(new_window, text='Месяц').grid(row=0, column=0)
        Entry(new_window, textvariable=month_var).grid(row=0, column=1)

        Label(new_window, text='Год').grid(row=1, column=0)
        Entry(new_window, textvariable=year_var).grid(row=1, column=1)

        Button(new_window, text='Ввести', command=submit).grid(row=2, column=1)

    def click_callback(self, mode):

        for widgets in self.chose_f.winfo_children():
            widgets.destroy()

        if mode == 'admin':
            a_button = Button(self.chose_f, text='Список читателей',
                              command=self.reader_list)
            a_button.pack(side=TOP, fill=BOTH, expand=1)

            b_button = Button(self.chose_f, text='Список книг',
                              command=self.book_list)
            b_button.pack(side=TOP, fill=BOTH, expand=1)

            c_button = Button(self.chose_f, text='Список читальных залов',
                              command=self.hall_list)
            c_button.pack(side=TOP, fill=BOTH, expand=1)

            d_button = Button(self.chose_f, text='Добавить читателя',
                              command=self.add_reader)
            d_button.pack(side=TOP, fill=BOTH, expand=1)

            e_button = Button(self.chose_f, text='Удалить читателя',
                              command=self.delete_reader)
            e_button.pack(side=TOP, fill=BOTH, expand=1)

            f_button = Button(self.chose_f, text='Добавить книгу',
                              command=self.add_book)
            f_button.pack(side=TOP, fill=BOTH, expand=1)

            g_button = Button(self.chose_f, text='Удалить книгу',
                              command=self.delete_book)
            g_button.pack(side=TOP, fill=BOTH, expand=1)

            h_button = Button(self.chose_f, text='Закрепить книгу',
                              command=self.fix_book)
            h_button.pack(side=TOP, fill=BOTH, expand=1)

            i_button = Button(self.chose_f, text='Открепить книгу',
                              command=self.unfix_book)
            i_button.pack(side=TOP, fill=BOTH, expand=1)

            j_button = Button(self.chose_f, text='Изменение шифра книги',
                              command=self.change_cipher)
            j_button.pack(side=TOP, fill=BOTH, expand=1)

            k_button = Button(self.chose_f, text='Какие книги закреплены за читателем',
                              command=self.books_fixed_to_reader)
            k_button.pack(side=TOP, fill=BOTH, expand=1)

            l_button = Button(self.chose_f, text='Как называется книга с заданным автором',
                              command=self.book_name_by_author)
            l_button.pack(side=TOP, fill=BOTH, expand=1)

            m_button = Button(self.chose_f, text='Какой шифр у книги с заданным названием',
                              command=self.cipher_by_book_name)
            m_button.pack(side=TOP, fill=BOTH, expand=1)

            n_button = Button(self.chose_f, text='Когда книга была закреплена за читателем',
                              command=self.fixation_date)
            n_button.pack(side=TOP, fill=BOTH, expand=1)

            o_button = Button(self.chose_f, text='Общее кол-во читателей',
                              command=self.readers_num)
            o_button.pack(side=TOP, fill=BOTH, expand=1)

            p_button = Button(self.chose_f, text='Наличие книг автора в чит. зале',
                              command=self.copies_by_author)
            p_button.pack(side=TOP, fill=BOTH, expand=1)

            q_button = Button(self.chose_f, text='Отчет о работе библиотеки за месяц',
                              command=self.month_report)
            q_button.pack(side=TOP, fill=BOTH, expand=1)

            self.chose_f.pack(side=TOP, fill=BOTH, expand=1, anchor=CENTER)
        elif mode == 'reg':
            a_button = Button(self.chose_f, text='Список читателей',
                              command=self.reader_list)
            a_button.pack(side=TOP, fill=BOTH, expand=1)

            b_button = Button(self.chose_f, text='Добавить читателя',
                              command=self.add_reader)
            b_button.pack(side=TOP, fill=BOTH, expand=1)

            c_button = Button(self.chose_f, text='Удалить читателя',
                              command=self.delete_reader)
            c_button.pack(side=TOP, fill=BOTH, expand=1)

            d_button = Button(self.chose_f, text='Закрепить книгу',
                              command=self.fix_book)
            d_button.pack(side=TOP, fill=BOTH, expand=1)

            e_button = Button(self.chose_f, text='Открепить книгу',
                              command=self.unfix_book)
            e_button.pack(side=TOP, fill=BOTH, expand=1)

            f_button = Button(self.chose_f, text='Какие книги закреплены за читателем',
                              command=self.books_fixed_to_reader)
            f_button.pack(side=TOP, fill=BOTH, expand=1)

            g_button = Button(self.chose_f, text='Когда книга была закреплена за читателем',
                              command=self.fixation_date)
            g_button.pack(side=TOP, fill=BOTH, expand=1)

            h_button = Button(self.chose_f, text='Общее кол-во читателей',
                              command=self.readers_num)
            h_button.pack(side=TOP, fill=BOTH, expand=1)

            self.chose_f.pack(side=TOP, fill=BOTH, expand=1, anchor=CENTER)
        else:
            a_button = Button(self.chose_f, text='Список книг',
                              command=self.book_list)
            a_button.pack(side=TOP, fill=BOTH, expand=1)

            b_button = Button(self.chose_f, text='Список читальных залов',
                              command=self.hall_list)
            b_button.pack(side=TOP, fill=BOTH, expand=1)

            c_button = Button(self.chose_f, text='Добавить книгу',
                              command=self.add_book)
            c_button.pack(side=TOP, fill=BOTH, expand=1)

            d_button = Button(self.chose_f, text='Удалить книгу',
                              command=self.delete_book)
            d_button.pack(side=TOP, fill=BOTH, expand=1)

            e_button = Button(self.chose_f, text='Изменение шифра книги',
                              command=self.change_cipher)
            e_button.pack(side=TOP, fill=BOTH, expand=1)

            f_button = Button(self.chose_f, text='Как называется книга с заданным автором',
                              command=self.book_name_by_author)
            f_button.pack(side=TOP, fill=BOTH, expand=1)

            g_button = Button(self.chose_f, text='Какой шифр у книги с заданным названием',
                              command=self.cipher_by_book_name)
            g_button.pack(side=TOP, fill=BOTH, expand=1)

            h_button = Button(self.chose_f, text='Наличие книг автора в чит. зале',
                              command=self.copies_by_author)
            h_button.pack(side=TOP, fill=BOTH, expand=1)

            self.chose_f.pack(side=TOP, fill=BOTH, expand=1, anchor=CENTER)


root = Tk()
root.title("База данных библиотеки")
root.minsize(400, 600)
app = MainApp(root)
app.pack(fill=BOTH, expand=1)

root.mainloop()
