

a=int(input("Enter the first number: "))
b=int(input("Enter the Second number: "))
if a>=5 and b >=5 :
    print("The numbers",a,"and",b,"are greater then or equal to five.")
else:
    print(f"The numbers {a} and {b} are lesser then five.")    

a=int(input("Enter the number: "))

if (a % 7 == 0):
    print(f"{a} is divisible by Seven")
else:
    print("Not Divisible by Seven")  

#Result annocement system

#NAME : MANI 1st year
#ROLL NUMBER : IT2112
#REGISTER NUMBER : 8115U21IT012

#NAME : BALA 2nd year
#ROLL NUMBER : AM2210
#REGISTER NUMBER : 8115U22AM010

year=int(input("Enter your year: "))
roll=input("Enter your roll number: ")
register=input("Enter your register number: ")

if(year==1):
    if(roll== "IT2111" and register=="8115U21IT011"):
        print("PASS")
    elif(roll=="IT2112" and register=="8115U21IT012"):
        print("FAIL")
    else:
        print(f"Either {roll} or {register} number is wrong")    
elif(year==2):
    if(roll== "AM2110" and register=="8115U21AM010"):
        print("FAIL")
    elif(roll=="AM2111" and register=="8115U21AM011"):
        print("PASS")
    else:
        print(f"Either {roll} or {register} number is wrong") 
else:
    print("Only 1st and 2nd year results has been annonced")        
