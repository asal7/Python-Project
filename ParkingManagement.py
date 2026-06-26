parking_list = []
while True:
    print("1: Enter car's plate: ")
    print("2: remove car")
    print("3: parking report: ")
    print("4: search car: ")
    print("0: exit")
    option = int (input("Enter your choice: "))
    print("------------------------------")

    match option:
        case 0:
            break
        case 1:
            plate = input("Enter plate: ")
            if plate not in parking_list:
                parking_list.append(plate)
                print("Your plate has been added to the parking list.")
            else:
                print("Your plate is already in the parking list.")
        case 2:
            plate = input("Enter plate: ")
            if plate in parking_list:
                parking_list.remove(plate)
                print("Your plate has been removed from the parking list.")
            else:
                print("Your plate is not in the parking list.")
        case 3:
            parking_list.sort()
            for plate in parking_list:
                print("plate no.: ", plate)
        case 4:
            plate = input("Enter plate: ")
            if plate in parking_list:
                print("Your plate is in the list: ", plate)
            else:
                print("Not found.")
        case _:
            print("Invalid option.")
    print("------------------------------")