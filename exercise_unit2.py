'''
Design an algorithm that reads a person's weight in pounds and returns their weight in kilograms.
Consider that
1 pound is equal to 0.453592 kilograms.
'''

'''
simple solution
n=int(input("input your weight in pounds: "))
total=n*0.453592    
print("your weight in kilograms is: " + str(round(total,2)))

'''


'''
solution with functions
def weight(pound):
    total=pound*0.453592
    print("su peso es de: " + str(round(total,2))+ " Kg")

weight(15)

'''
'''
call a function in other function
def hi():
    print("input your weight in pounds: ")
    
def weight():
    hi()
    pound=float(input())
    total=pound*0.453592
    print("su peso es de: " + str(round(total,2))+ " Kg")
    
weight()

'''

'''
nested functions
def hi():
    pound=input("input your weight in pounds: ")
    def weight():
        total=float(pound)*0.453592
        print("su peso es de: " + str(round(total,2))+ " Kg")
    weight()
        
hi()
'''
