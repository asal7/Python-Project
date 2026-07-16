from tkinter import *
from tkinter import messagebox
from tkinter import ttk

product_list = []

def save_click():
    product = {
        "id": id.get(),
        "name": name.get(),
        "quantity": quantity.get(),
        "price": price.get(),
    }

    table.insert("", END, values=tuple(product.values()))
    product_list.append(product)

    messagebox.showinfo("Save", "Product saved successfully")

    id.set(id.get() + 1)
    name.set("")
    quantity.set(0)
    price.set(0)

window = Tk()
window.title("Store Information")
window.geometry("580x310")

Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=80, y=60)

Label(window, text="Quantity").place(x=20, y=100)
quantity = IntVar(value=1)
Entry(window, textvariable=quantity).place(x=80, y=100)

Label(window, text="Price").place(x=20, y=140)
price = IntVar(value=0)
Entry(window, textvariable=price).place(x=80, y=140)

table = ttk.Treeview(window, height=12, columns=[1, 2, 3, 4], show="headings")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=80)
table.column(4, width=80)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Quantity")
table.heading(4, text="Price")

table.place(x=230, y=20, width=330)

Button(
    window,
    text="Save",
    width=10,
    command=save_click
).place(x=70, y=260)

window.mainloop()