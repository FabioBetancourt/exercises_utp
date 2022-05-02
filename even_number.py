

n=int(input("input a number: "))
r=n%2

if  n<0:
    print("input another number: ")
elif r==0:
    print("the number " + str(n) + " is a even numer")
else:
    print("the number " + str(n) + " is not a even number") 