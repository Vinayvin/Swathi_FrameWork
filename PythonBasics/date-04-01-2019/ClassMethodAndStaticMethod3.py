from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def checkAgeValidToVote(age):
        if age > 18:
            return "valid age to vote"
        else:
            return "Not eleigle to vote"


    @classmethod
    def getAgefromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

p1=Person("john",25)
print(p1.age)
p2 = Person.getAgefromBirthYear('Pranav', 1993)
print(p2.name)
print(p2.age)
print(Person.getAgefromBirthYear('Sam',1993))
print(Person.checkAgeValidToVote(17))
