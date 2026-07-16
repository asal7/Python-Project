from tkinter import *
from tkinter import messagebox
from tkinter import ttk

lesson_list = []

def calculate_total(lesson_list):
    return sum(map(lambda lesson: lesson["unit"], lesson_list))

def save_click():
    lesson = {
        "id": id.get(),
        "name": name.get(),
        "teacher": teacher.get(),
        "unit": unit.get(),
    }

    if calculate_total(lesson_list) + lesson["unit"] <= 17:
        table.insert("", END, values=tuple(lesson.values()))
        lesson_list.append(lesson)
        messagebox.showinfo("Save", "Lesson saved successful")
        id.set(id.get() + 1)
        unit.set(2)
        teacher.set("")
        name.set("")
    else:
        messagebox.showerror("Save Error","Cant take more lesson !")

window = Tk()
window.title("Lesson Information")
window.geometry("580x310")

Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=80, y=60)

Label(window, text="Teacher").place(x=20, y=100)
teacher = StringVar()
Entry(window, textvariable=teacher).place(x=80, y=100)

Label(window, text="Unit").place(x=20, y=140)
unit = IntVar(value=2)
ttk.Combobox(window, values=[1, 2, 3, 5], width=17, textvariable=unit, state="readonly").place(x=80, y=140)

table = ttk.Treeview(window, height=12, columns=[1, 2, 3, 4], show="headings")
table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Teacher")
table.heading(4, text="Unit")

table.place(x=230, y=20, width=330)

Button(
    window,
    width=10,
    text="ذخیره",
    command=save_click,
).place(x=70, y=260)

window.mainloop()