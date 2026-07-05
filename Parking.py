Parking_List = []
while True:
    print("1: Enter to Parking ")
    print("2: Exit from Parking ")
    print("3: Find by plate ")
    print("4: Parking List: ")
    print("0: exit")
    option = int (input("Enter your choice: "))
    print("------------------------------")

    match option:
        case 0:
            break
        case 1:
            for i in range(4):
                Brand = input("Enter Car Brand: ")
                Model = int(input("Enter Car Model: "))
                Color = input("Enter Car's Color: ")
                Plate = input("Enter Car's Plate: ")
                Car_Info = {
                    "Brand": Brand,
                    "Model": Model,
                    "Color": Color,
                    "Plate": Plate
                }
                if Car_Info not in Parking_List:
                    Parking_List.append(Car_Info)
                    print("Your plate has been added to the parking list.")
                    break
                else:
                    print("Your plate is already in the parking list.")
        case 2:
            plate_remove = input("Enter Car's plate: ")
            for car in Parking_List:
                if car['Plate'] == plate_remove:
                    Parking_List.remove(car)
                    print("Your plate has been removed from the parking list.")
                    break
            else:
                print("Your plate is not in the parking list.")
        case 3:
            Car_Plate = input("Enter Car's Plate: ")
            found = False
            for car in Parking_List:
                if car['Plate'] == Car_Plate:
                    print(f"{Car_Info['Plate']:10}" "has been found in the parking list.")
                    found = True
                    break
            if not found:
                print("Your plate is not in the parking list.")
        case 4:
            for car in Parking_List:
                print(f"{car['Plate']:10} - " f"{car['Brand']:10}" f"({car['Model']:10}) " f" - {car['Color']:10}")
        case _:
            print("Invalid option.")
    print("------------------------------")