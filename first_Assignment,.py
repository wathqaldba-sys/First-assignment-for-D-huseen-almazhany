students = []


def add_student():
    i = input("Student ID: ")

    for s in students:
        if s["id"] == i:
            print("ID already exists")
            return

    n = input("Student Name: ")
    g = float(input("Student Grade: "))

    students.append({
        "id": i,
        "name": n,
        "grade": g
    })

    print("Student added")


def show_students():
    if len(students) == 0:
        print("No students")
        return

    for s in students:
        print("----------------")
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Grade:", s["grade"])


def search_student():
    i = input("Enter ID: ")

    for s in students:
        if s["id"] == i:
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Grade:", s["grade"])
            return

    print("Student not found")


def update_grade():
    i = input("Enter ID: ")

    for s in students:
        if s["id"] == i:
            s["grade"] = float(input("New Grade: "))
            print("Grade updated")
            return

    print("Student not found")


def delete_student():
    i = input("Enter ID: ")

    for s in students:
        if s["id"] == i:
            students.remove(s)
            print("Student deleted")
            return

    print("Student not found")


def average_grade():
    if len(students) == 0:
        print("No students")
        return

    t = 0

    for s in students:
        t = t + s["grade"]

    a = t / len(students)

    print("Average =", a)


def best_student():
    if len(students) == 0:
        print("No students")
        return

    b = students[0]

    for s in students:
        if s["grade"] > b["grade"]:
            b = s

    print("Best Student")
    print("Name:", b["name"])
    print("Grade:", b["grade"])


def worst_student():
    if len(students) == 0:
        print("No students")
        return

    w = students[0]

    for s in students:
        if s["grade"] < w["grade"]:
            w = s

    print("Worst Student")
    print("Name:", w["name"])
    print("Grade:", w["grade"])


def total_students():
    print("Total Students =", len(students))


def passed_students():
    if len(students) == 0:
        print("No students")
        return

    for s in students:
        if s["grade"] >= 60:
            print(s["name"], s["grade"])


def failed_students():
    if len(students) == 0:
        print("No students")
        return

    for s in students:
        if s["grade"] < 60:
            print(s["name"], s["grade"])


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Calculate Average Grade")
    print("7. Show Best Student")
    print("8. Show Worst Student")
    print("9. Show Total Students")
    print("10. Show Passed Students")
    print("11. Show Failed Students")
    print("12. Exit")

    c = input("Choose: ")

    if c == "1":
        add_student()

    elif c == "2":
        show_students()

    elif c == "3":
        search_student()

    elif c == "4":
        update_grade()

    elif c == "5":
        delete_student()

    elif c == "6":
        average_grade()

    elif c == "7":
        best_student()

    elif c == "8":
        worst_student()

    elif c == "9":
        total_students()

    elif c == "10":
        passed_students()

    elif c == "11":
        failed_students()

    elif c == "12":
        print("Good Bye")
        break

    else:
        print("Wrong Choice")