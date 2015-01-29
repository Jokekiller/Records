class Workers():
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None

employee = Workers()
employee.name = input("Enter your name: ")
employee.number = input("Enter you employee number: ")
employee.hour =int(input("Enter the number of hours worked this week: "))
employee.pay = float(input("Enter your hourly rate: "))

totalPay = employee.hour * employee.pay
print("*"*30)
print("*Pay Slip                    *")
print("*Name: {0}                 *".format(employee.name))
print("*Employee Number: {0}    *".format(employee.number))
print("*Hours worked: {0}            *".format(employee.hour))
print("*Rate of Pay: {0}          *".format(employee.pay))
print("*Total Pay: {0}            *".format(totalPay))
print("*"*30)
