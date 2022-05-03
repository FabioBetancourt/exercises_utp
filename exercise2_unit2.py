'''
Design an algorithm to calculate the length of the hypotenuse (i.e. the longest side of a right triangle, opposite the right angle) 
using the Pythagorean Theorem:
c = √a2 + b2
Consider that To compute a square root, the entire formula has to be raised to 0.5, in Python
it would be **0.5, where the mathematical operator would be **exponent.
'''

import math

def pit(a,b):
    c=math.sqrt(a)+math.sqrt(b)
    print("the length of the hypotenuse is: " + str(round(c,4)))
    
    
pit(5,6)
    
