#Harry Robinson
#26-01-2015
#Student name and results
class studentMarks:
    def __init__(self):
        self.studentName = None
        self.score = None

names = []
for count in range(4):
    name = studentMarks()
    name.studentName = input("Enter the name of the student: ")
    name.score = int(input("Enter the score the student got: "))
    names.append(name)

#names = []
#for count in range(4):
#    names.append(studentMarks())

print("|Student Name|Score|")
for name in names:
    print("{0:^6}{1:^8}".format(name.studentName, name.score))
    
