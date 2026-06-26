lesson_list = []
sum_lesson = 0
while True:
    print("1) Add Lesson")
    print("2) Report")
    print("0) Exit")

    option = int(input("Enter your option: "))
    print("-------------------------")

    if option == 0:
        break

    elif option == 1:
        lesson = int(input("Enter lesson number(1,2,3,5): "))
        sum_lesson = sum(lesson_list)
        if lesson in [1,2,3,5] and sum_lesson <= 17:
            lesson_list.append(lesson)
            print("lesson number added")
        else:
            print("lesson number not added, sum is greater than 17")

    elif option == 2:
        lesson_list.sort()
        print("lesson number list", lesson_list)
        for lesson in lesson_list:
            print(f"{lesson:10} {lesson_list.count(lesson) * '*'}")
        print("-------------------------")

        print("Sum:", sum_lesson)
    else:
        print("Invalid option")

    print("-------------------------")