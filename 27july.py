# def function(a=9):
#     print(a)
# b=function()
# print(b)

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter the value n: "))
# print(f"The factorial of {n} is",fact(n))        

# a=5

# def fun():
#     global b
#     b=7
#     print(a,b)
# fun()
# print(b)    


# from mypackage import *


# a=number("Enter the number: ")
# b=string("Enter the string: ")

# d(a)


# d(b)

# from math import *

# print(pi)

# print(sqrt(81))

# import random

# for i in range (10):
#     value=random.randint(1,100)
#     print(value,end=" ")

# import calendar

# print(calendar.month(2023,8))

# import datetime

# def showmessage(meg):
#     print(meg)
# showmessage("hello") 

# def showmessage(meg):
#     now=datetime.datetime.now()
#     print(meg)
#     print(str(now))
# showmessage("current date and time : ")

# now=datetime.datetime.now()
# print(str(now))

# import urllib.request

# a=urllib.request.urlopen('https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458712209&hvpos=&hvnetw=g&hvrand=6321153976701479799&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9152952&hvtargid=kwd-10573980&hydadcr=14453_2154373')
# print(a.read())

# try:
#     x=int(input("Enter the number: "))
#     print(x)
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")    
# finally:
#     print("code finished")        

# a=open("/home/nesh/Desktop/ONLINE COURSE/newfile.txt","r")
# print(a)
# a.close()