class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

students = []
teachers = []


def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    students.append(Student(name, age))
    print("Student added successfully.")


def add_teacher():
    name = input("Enter teacher's name: ")
    subject = input("Enter teacher's subject: ")
    teachers.append(Teacher(name, subject))
    print("Teacher added successfully.")


def display_students():
    if not students:
        print("No students available.")
    else:
        print("\n--- Students ---")
        for student in students:
            print(f"Name: {student.name}, Age: {student.age}")


def display_teachers():
    if not teachers:
        print("No teachers available.")
    else:
        print("\n--- Teachers ---")
        for teacher in teachers:
            print(f"Name: {teacher.name}, Subject: {teacher.subject}")


def main():
    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Display Students")
        print("4. Display Teachers")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_teacher()
        elif choice == "3":
            display_students()
        elif choice == "4":
            display_teachers()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()