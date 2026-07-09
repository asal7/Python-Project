lessons_list = [
    {"id":1, "name": "python", "unit":2},
    {"id":2, "name": "java", "unit":3},
    {"id":3, "name": "c++", "unit":5}
]

lesson_id= int(input("Enter the lesson id: "))
lesson_name = input("Enter the name of the lesson: ")
lesson_unit = int(input("Enter the unit of the lesson: "))

new_lesson = {"id":lesson_id,"name":lesson_name, "unit":lesson_unit}

def get_names(lesson):
    return lesson["name"]
lesson_names = list(map(get_names, lessons_list))

def get_unit(lesson):
    return lesson["unit"]
total_units = sum(map(get_unit, lessons_list))

if lesson_name in lesson_names:
    print("Lesson already exists!")
elif total_units + lesson_unit > 17:
    print("Error: The Maximum number of units is 17.")
else:
    lessons_list.append(new_lesson)
    print("Lesson added successfully!")

def sort_lessonName(lesson):
    return lesson["name"]
sorted_lesson = sorted(lessons_list, key=sort_lessonName)
for lesson in sorted_lesson:
    #print(lesson)
    print(f"{lesson['id']:3}" + "-" + f"{lesson['name']:5}" + "-" + f"{lesson['unit']:3}")

