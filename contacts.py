from contacts_module import *

while True:
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
            print("Error: Invalid option!")