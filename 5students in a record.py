#Harry Robinson
#30-01-2015
#Storing 5 students and the marks the gained in 4 modules

class student():
    def __intit__(self):
        self.name = None
        self.marks = None
        self.modules = None

student_info = []
for count in range (2):
    info = student()
    info.modules = []
    info.marks = []
    info.name = input("Enter the students Name: ")
    for score in range (2):
        module = input("Enter the module that student took: ")
        info.modules.append(module)
        mark = int(input("Enter the score they got on that module: "))
        info.marks.append(mark) 
    student_info.append(info)
total = 0
for mark in info.marks:
    total = total + mark
    meanMark = total / 2
print("Mean mark is {0}".format(meanMark))
print("|Student Name| Modules | Mark|")
print("-"*30)
for info in student_info:
    print("|{0:<12}|".format(info.name))
    studentTotal = 0
    for index in range(2):
        print("             |{0:<9}|{1:<6}|".format(info.modules[index], info.marks[index]))
        studentTotal =  (studentTotal + info.marks[index]) / 2
    if studentTotal > meanMark:
        differenceMark = studentTotal - meanMark
        print("Total mean mark is {0}, you were {1} above the mean mark {2}".format(studentTotal, differenceMark, meanMark))
    elif meanMark > studentTotal:
        differenceMark = meanMark - studentTotal
        print("Total mean mark is {0}, you were {1} below the mean mark {2}".format(studentTotal, differenceMark, meanMark))
