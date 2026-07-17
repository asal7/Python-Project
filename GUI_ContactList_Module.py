from tkinter import *
from tkinter import messagebox


def save_click(tb,name_var,family_var, number_var,phone_type_var, contact_list):
    contact = {"name": name_var.get(),
               "family": family_var.get(),
               "number": number_var.get(),
               "phone_type": phone_type_var.get()}

    for user in contact_list:
        if user['name'] == contact['name'] and user['family'] == contact['family'] and user['number'] == contact['number']:
            messagebox.showerror("Error", "Contact already exists!")
            break
    else:
        tb.insert("", END, values=tuple(contact.values()))
        contact_list.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")


