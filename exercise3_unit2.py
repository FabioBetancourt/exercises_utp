'''
Design an algorithm that allows to do the following conversion
• Miles to kilometers.
• Kilometers to miles.
Consider that
1 mile is 1.60934 kilometers
1 kilometer is 0.621371 miles
'''
'''
#simple solution
op=input("if you want convert miles to km write 'miles' or if you want convert km a miles write 'km': ")

if op == "km":
    n=input("Input the km: ")
    ml=float(n)*0.62137
    print("for " + str(n) + " km, the valou in miles is " + str(ml))
elif op == "miles":
    n=input("Input the miles: ")
    km=float(n)*1.60934
    print("for " + str(n) + " miles, the valou in miles is " + str(km))
else:
    print("input only 'miles' or 'km'")
    

'''
'''
# solution with simple funtions
def convert() :
    ent=input("Input 1 for a milles to kilometers or 2 for kilometers to miles: ")
    if int(ent) >2 or int(ent) <1:
        print("input only 1 or 2")
    elif int(ent)==1:
        n=input("Input the miles: ")
        km=float(n)*1.60934
        print("for " + str(n) + " miles, the valou in miles is " + str(km))
    else:
        n=input("Input the km: ")
        ml=float(n)*0.62137
        print("for " + str(n) + " km, the valou in miles is " + str(ml))
convert()
'''
'''
# call a function in other function

def convert():
    print("Input 1 for a milles to kilometers or 2 for kilometers to miles: ")

def convert1():
    print("enter the miles: ")

def convert2():
    print("enter the km: ")

def convert3():
    convert()
    ent=int(input())
    if ent==1:
        convert1()
        n=(float(input()))
        km=n*1.60934
        print("for " + str(n) + " miles, the valou in miles is " + str(km))
    else:
        convert2()
        n=(float(input()))
        km=n*0.62137
        print("for " + str(n) + " miles, the valou in miles is " + str(km))
        
convert3()
'''

#nested functions
