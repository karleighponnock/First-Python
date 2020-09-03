#calculator

#import regex
import re

print("Python Calculator")
print("Type `quit` to exit\n")

previous = 0
run = True

def performMath():
    global run
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
         print("You typed", equation)

while run:
    performMath()