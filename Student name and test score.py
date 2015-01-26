#Harry Robinson
#26-01-2015
#Student name and results
class studentMarks:
    def __init__(self):
        self.studentName = None
        self.score = None
name = studentMarks()
for count in range(4):    
    name.studentName = input("Enter the name of the student: ")
    name.score = int(input("Enter the score the student got: "))

names = []
for count in range(4):
    names.append(studentMarks)
    count = count + 1

print("|Student Name|Score|")
for index in range (4):
    print("|{0:^12}|{1:^5}|".format(name.studentName, name.score))
    index = index + 1
    print(names[index].number)
    
