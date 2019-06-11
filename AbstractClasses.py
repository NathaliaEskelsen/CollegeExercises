from abc import ABC, abstractmethod
class  Assessment(ABC):

    def __init__(self, studentName, studentID, result):
        self.name = studentName
        self.id = studentID
        if result < 0 or result > 100:
            self.grade = 0
        else:
            self.grade = result

    @abstractmethod
    def print(self):
        print("Student Name:", self.name)
        print("Student Id:", self.id)
        print("Student Grade:",self.grade)

class CA(Assessment):

    def __init__(self, studentName, studentID, result, elapsed_days):
        super().__init__(studentName, studentID,result)
        self.elapsedDays = elapsed_days

    def print(self):
        print("****************************")
        super().print()
        print("Elapsed Days:",self.elapsedDays)
        print("****************************")

class Examination(Assessment):
    def __init__(self, studentName, studentID, result, date_in, time_in):
        super().__init__(studentName, studentID,result)
        self.date = date_in
        self.time = time_in

    def print(self):
        print("****************************")
        super().print()
        print("Date:",self.date)
        print("Time:",self.time)
        print("****************************")

ca1 = CA("Nathalia Eskelsen","X00151868",97,14)
ca2 = CA("Nathalia Eskelsen","X00151868",98,0)
examination1 = Examination("Nathalia Eskelsen", "X00151868",100,"30/10/1997","09:30")
ca1.print()
ca2.print()
examination1.print()
finalGrade = ((ca1.grade * 0.25) + (ca2.grade * 0.25) + (examination1.grade * 0.5)) * 1
print("****************************")
print("Overal Grade:",finalGrade)
print("****************************")

list = []
for i in range(3):
    assessment = int(input("Please inform the type of assessment! Type '1' for Examination and '2' for CA"))
    if assessment == 1:
        name = input("Insert student name:")
        id = input("Insert student Id:")
        grade = int(input("Insert grade:"))
        date = input("Insert the date:")
        time = input("Insert the time:")
        examination = Examination(name,id,grade,date,time)
        list.append(examination)
        print("Examination added!")
    elif assessment == 2:
        name = input("Insert student name:")
        id = input("Insert student Id:")
        grade = int(input("Insert grade:"))
        days = int(input("Insert elapsed days:"))
        ca = CA(name, id, grade, days)
        list.append(ca)
        print("CA added!")

for item in list:
    item.print()
