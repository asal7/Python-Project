product_list = []

def show_menu_item():
    """
    menu
    """
    print("1) Add product")
    print("2) Show orders")
    print("3) Find by name")
    print("0) Exit")
    option = int(input("Enter your choice: "))
    print("-" * 20)
    return option

def show_order_list (order_list):
    print("Products of your order:")
    for product in order_list:
        total = product['quantity'] * product['price']
        print(f"{product['name']:10} {product['brand']:10} {product['quantity']:3} * {product['price']:5} ==> {total:8} $")
    print("-" * 50)
    print("Total: ", "\t" * 8 , calculate_total(order_list))

def calculate_total (order_list):
    sum_total = 0
    for product in order_list:
        total = product['quantity'] * product['price']
        sum_total += total
    return sum_total


def find_product_by_name(order_list, product_name):
    for product in product_list:
        if product['name'] == product_name:
            return product
    else:
        return None