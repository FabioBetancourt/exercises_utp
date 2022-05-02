'''
read two integers
positive and determine if the
last digit of a number is
equal to the last digit of the other.
'''




n1=int(input("input a number: "))
n2=int(input("input other number: "))
u1=n1%10
u2=n2%10
if n1<0:
    n1=n1*(-1)
elif n2<0:
    n2=n2*(-1)
elif u1==u2:
    print("the last digit of a number is equal to the last digit of the other")
else: 
    print("the last digit of a number is not equal to the last digit of the other")