# class Student:
#     def StudentDetails(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
# s1=Student()
# s1.StudentDetails("sathish","r25",'550')      
# print(s1.marks)


class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display_details(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)
s1=Student("Sathish","R255","598")
s1.display_details()