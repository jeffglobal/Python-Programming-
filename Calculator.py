'''
    Program: Calculator
    Author: Jeffrey Spinner
    © 2018
'''

import re

print("Jeff's Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run      # Get a global variable into your local function
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print('ByeBye')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)





while run:
    performMath()