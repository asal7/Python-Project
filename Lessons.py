my_file = open("LessonsList.txt","a+")
lessons_list = []

while True:
    print("1) Add lesson")
    print("2) Print lessons List")
    print("3) Find By Teacher")
    print("0) Exit")

    option = input("Enter your option: ")
    print("---------------------------------------------")
    if option == "1":
        code = int(input("Enter Code : "))
        title = input("Enter Title : ")
        teacher = input("Enter Teacher's Name : ")
        unit = int(input("Enter Unit : "))

        #Checking whether the unit value entered by the user is valid.
        if unit not in (1, 2, 3, 5):
            print("Error: The number of units can only be 1, 2, 3, or 5.")
            continue

        #Calculation of total units
        total_units = 0
        for lesson in lessons_list:
            total_units += lesson["unit"]

        #Checking whether the total units is greater than 17 or not
        if total_units + unit > 17:
            print("Error: The maximum number of units allowed is 17.")
            print("Units obtained:", total_units)
            print("Maximum selectable units:", 17 - total_units)

        else:
            lesson = {"code": code, "title": title, "teacher": teacher, "unit": unit}
            print(lesson)
            lessons_list.append(lesson)
            my_file.write(str(lesson) + "\n")
            print("Lesson added successfully.")

    elif option == "2":
        # Printing lesson list from my_file
        my_file.seek(0)
        all_lessons = my_file.readlines()
        for lesson in all_lessons:
            print(lesson.strip())

        #Normal printing lesson list
        if len(lessons_list) == 0:
            print("No Lessons!")
            continue

        print("Lessons List")
        print("---------------------------------------------")
        total_units = 0
        for lesson in lessons_list:
            print(f"Title: {lesson['title']}, teacher: {lesson['teacher']}, unit: {lesson['unit']}")

            total_units += lesson["unit"]

        print("-" * 40)
        print("Total Units =             ", total_units)

    elif option == "3":
        teacher_name = input("Enter Teacher's Name : ")
        found = False
        for lesson in lessons_list:
            if lesson["teacher"] == teacher_name:
                lesson = {
                    "code": lesson["code"],
                    "title": lesson["title"],
                    "teacher": lesson["teacher"],
                    "unit": lesson["unit"]
                }

                print(f"{lesson['title']:10}" + "by " + f"{lesson['teacher']:10}" + f"{lesson['unit']:3}")
                found = True
        if not found:
            print("Teacher Not Found")

    elif option == "0":
        print("Exiting ...")
        break
    else:
        print("Invalid option")

    print("---------------------------------------------")

my_file.close()



