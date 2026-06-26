from unittest import case

from store_module import *

while True:
    option = show_menu_item()
    match option:
        case 1:
            name = input("Enter product name: ")
            brand = input("Enter brand: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if not find_product_by_name(product_list, name):
                product = {"name": name, "brand": brand, "quantity": quantity, "price": price}
                product_list.append(product)
                print("Product is added.")
            else :
                print("Error: Product with that name already exists")
        case 2:
            show_order_list(product_list)
        case 3:
            name = input("Enter product name: ")
            product = find_product_by_name(product_list, name)
            if product:
                print("Found: ", product)
            else:
                print("Error: Product Not Found!!!")
        case 0:
            print("Exiting ...")
            break
        case _:
            print("Error: Invalid option!!!")
    print("-" * 20)