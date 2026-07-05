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
                Plate = input("Enter Price of product: ")
                Car_Info = {
                    "Brand": Brand,
                    "Model": Model,
                    "Color": Color,
                    "Plate": Plate
                }
                if Car_Info['Plate'] not in Parking_List:
                    Parking_List.append(Car_Info)
                    print("Your plate has been added to the parking list.")
                else:
                    print("Your plate is already in the parking list.")