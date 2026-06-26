contact_list = []

def show_menu():
    """
    menu
    """
    print("1) Add Contact:")
    print("2) Find By Family:")
    print("3) Find By Number:")
    print("4) Show List:")
    print("0) Exit")
    option = int(input("Enter your choice: "))
    print("-" * 30)
    return option

def find_contact_by_family(phone_list, contact_family):
    for contact in contact_list:
        if contact["family"] == contact_family:
            return contact
    else:
        return None


def find_contact_by_number(phone_list, contact_number):
    for contact in contact_list:
        if contact["number"] == contact_number:
            return contact
    else:
        return None

def show_contact_list(phone_list):
    print(f"{'Name':<15}{'Family':<15}{'Number':<15}{'Type':<15}")
    print("-" * 60)

    for contact in phone_list:
        print(
            f"{contact['name']:<15}"
            f"{contact['family']:<15}"
            f"{contact['number']:<15}"
            f"{contact['phone_type']:<15}"
        )


