#calculator

#import regex
import re

print("Python Calculator")
print("Type `quit` to exit\n")

previous = 0
run = True

def performMath():
    #access variables globally
    global run
    global previous
    #if just starting ask for equation
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    #if an operation has been done print the previous answer
    else:
        equation = input(str(previous))
    #if user tyoes exit end app
    if equation == 'quit':
        print("Goodbye")
        run = False
    #remove everything other than numbers or operators from user input
    #evaluate it and print new answer
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        
     

while run:
    performMath()