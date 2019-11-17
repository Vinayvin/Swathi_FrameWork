class Student:
    name='sam'
    Id=1001
    def stud_details(self):
        print(self.name)
        print(self.Id)


class Marks:
    mark=23
    def stud_details(self):
        print(self.mark)


class Result(Student,Marks):
    def stud_details(self):
        print(self.name)
        print(self.Id)
        print(self.mark)



ob=Result()
ob.stud_details()













