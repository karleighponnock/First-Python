#calculator

#import regex
import re

print("Python Calculator")

previous = 0
run = True

def performMath():
    equation = input("Enter equation:")
    print("You typed", equation)
    
while run:
    performMath()