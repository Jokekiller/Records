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

print("|Student Name|Score|")
print("-"*20)
for name in names:
    print("|{0:^12}|{1:^5}|".format(name.studentName, name.score))
    print("-"*20)

