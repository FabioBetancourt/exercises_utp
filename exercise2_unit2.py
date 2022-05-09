'''
Design an algorithm to calculate the length of the hypotenuse (i.e. the longest side of a right triangle, opposite the right angle) 
using the Pythagorean Theorem:
c = √a2 + b2
Consider that To compute a square root, the entire formula has to be raised to 0.5, in Python
it would be **0.5, where the mathematical operator would be **exponent.
'''


'''
#simple solution
a=input("input a Hick opposite: ")
b=input("input a Hick adyacent: ")

c=(((float(a)**2)+(float(b)**2)))**0.5
print("the lenght of the hypotenuse is: " + str(round(c,3)))
'''



'''

import math
#solution with simple funtions
def pit(a,b):
    c=math.sqrt(a*a)+math.sqrt(b*b)
    print("the length of the hypotenuse is: " + str(round(c,4)))
    
pit(5,6)

'''
'''
# call a function in other function
import math
def message1():
    print("input a Hick opposite: " )

def message2():
    print("input a Hick adyacent: " )

def operator():
    message1()
    b=float(input())
    message2()
    a=float(input())
    c=math.sqrt((a**2)+(b**2))
    print("the length of the hypotenuse is: " + str(round(c,4)))
    
operator()
'''
'''
#nested functions
import math
def message1():
    a=input("input a Hick opposite: " )
    b=input("input a Hick adyacent: " )
    def operator():
        c=math.sqrt((float(a)**2)+(float(b)**2))
        print("the length of the hypotenuse is: " + str(round(c,4)))
    operator()
           
message1()
'''