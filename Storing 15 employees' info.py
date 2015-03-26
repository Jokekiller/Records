#Harry Robinson
#26-03-2015
#Storing 15 employees information

class Employee:
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None
def getEmployeeInfo(employees):
    for count in range (15):
        detail= Employee()
        detail.name = input("Enter their name: ")
        detail.number = input("Enter their employee number: ")
        detail.hours = float(input("Enter the number of hours worked this week: "))
        detail.pay = float(input("Enter their hourly rate: "))
        employees.append(detail)
    return employees
def main():
    employees = []
    employees = getEmployeeInfo(employees)
    name_search = input("enter a name you want to search: ")
    found = False
    index = 0
    while not found and index < 15:
        employee = employees[index]
        if name_search == employee.name:
            print("found")
            print()
            print("*"*30)
            print("*Pay Slip*")
            print("*Name: {0}".format(employee.name))
            print("*Employee Number: {0}".format(employee.number))
            print("*Hours worked: {0}".format(employee.hours))
            print("*Rate of pay: {0}".format(employee.pay))
            print("*"*30)
            found = True

        else:
            print("Not Found")
            index = index + 1

#main
main()
        
