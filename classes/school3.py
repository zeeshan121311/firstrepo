class School:
    pass

class Student(School):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_number,
        student_address,
        student_fees
        ):

        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees

    def getStudent(self):
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fees = {self.student_fees},"
    
class Teacher(School):
    pass

class Classroom(School):
    pass
class Admin(School):
    pass

    
student1 = Student(
    "1",
    "Zeeshan",
    "Saeed",
    "03112489345",
    "G 125 Street 03 Manzoor Colony Karachi",
    "2000",
    )

z = student1.getStudent()
print(z)