#Harry Eobinson
#10/3/2015
#Records class exercises

import random
class draw:
    def __init__(self):
        self.drawNumbers = None
        self.date = None

numbers = []
draws = []
aDraw = draw()
date_entered = input("Enter the date you want to store: ")
aDraw.date = date_entered
for count in range (6):
    number_entered = random.randrange(1,49)
    numbers.append(number_entered)
print(aDraw.date, numbers)


