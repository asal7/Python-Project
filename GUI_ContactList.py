from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from  GUI_ContactList_Module import *

contact_list = []

window = Tk()
window.title("Contact List")
window.geometry("600x350")

Label(window, text="firstname:").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=20)

Label(window, text="familyname:").place(x=20, y=60)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=60)

Label(window, text="number:").place(x=20, y=100)
number = StringVar()
Entry(window, textvariable=number).place(x=100, y=100)

Label(window, text="phone type:").place(x=20, y=140)
phone_type = StringVar()
Entry(window, textvariable=phone_type).place(x=100, y=140)

tb = ttk.Treeview(window, height=12, columns=[1,2,3,4], show='headings')
tb.column(1, width=60)
tb.column(2, width=100)
tb.column(3, width=80)
tb.column(4, width=80)

tb.heading(1, text="Name")
tb.heading(2, text="Family")
tb.heading(3, text="Number")
tb.heading(4, text="Phone Type")

tb.place(x=250, y=20, width=330)

Button(window, text="Save", width=10, bg="green yellow", command=lambda: save_click(
    tb,
    name,
    family,
    number,
    phone_type,
    contact_list
)).place(x=100, y=180)

"""while True:
    option = show_menu()
    match option:
        case 1:
            name = input("Enter firstname: ")
            family = input("Enter family name: ")
            number = int(input("Enter number: "))
            phone_type = input("Enter phone type: ")

            for contact in contact_list:
                if contact['name'] == name and contact['family'] == family and contact['phone_type'] == phone_type:
                    print("Error: Contact already exists!")
                    break
            else:
                contact = {"name": name, "family": family, "number": number, "phone_type": phone_type}
                contact_list.append(contact)
                print("Contact added!")
            print("-" * 40)

        case 2:
            family = input("Enter family name: ")
            contact = find_contact_by_family(contact_list, family)
            if contact:
                print("Contact found: ", contact)
            else:
                print("Error: Contact not found!")
            print("-" * 40)
        case 3:
            number = int(input("Enter number: "))
            contact = find_contact_by_number(contact_list, number)
            if contact:
                print("Contact found: ", contact)
            else:
                print("Error: Contact not found!")
            print("-" * 40)
        case 4:
            show_contact_list(contact_list)
            print("-" * 40)
        case 0:
            print("Exiting...")
            break
        case _:
            print("Error: Invalid option!")"""
window.mainloop()