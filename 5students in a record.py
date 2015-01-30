#Harry Robinson
#30-01-2015
#Storing 5 students and the marks the gained in 4 modules

class student():
    def __intit__(self):
        self.name = None
        self.marks = None
        self.modules = None

student_info = []
for count in range (5):
    info = student()
    info.modules = []
    info.marks = []
    info.name = input("Enter the students Name: ")
    for score in range (4):
        module = input("Enter the module that student took: ")
        info.modules.append(module)
        mark = int(input("Enter the score they got on that module: "))
        info.marks.append(mark)
    student_info.append(info)
print("|Student Name| Modules | Mark|")
print("-"*30)
for info in student_info:
    print("|{0:<12}|".format(info.name))
    for index in range(4):
            print("             |{0:<9}|{1:<6}|".format(info.modules[index], info.marks[index]))
