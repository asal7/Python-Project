product_list = []
while True:
    print("1: Add product: ")
    print("2: Product list")
    print("0: Exit ")
    option = int(input("Enter your choice: "))
    print("------------------------------")
    match option:
        case 0:
            break
        case 1:
            for i in range(4):
                Name = input("Enter Product name: ")
                Brand = input("Enter Brand name: ")
                Quantity = int(input("Enter Quantity of product: "))
                Price = float(input("Enter Price of product: "))
                prd = {
                "Name": Name,
                "Brand": Brand,
                "Quantity": Quantity,
                "Price": Price
                        }
                product_list.append(prd)
        case 2:
            for product in product_list:
                multi = product['Quantity'] * product['Price']
                print(f"{product['Name']:10} {product['Brand']:10}" 
                f"{product['Quantity']:3} * {product['Price']:5.2f} => { multi:.2f}")
        case _:
            print("Invalid option.")
    print("------------------------------")