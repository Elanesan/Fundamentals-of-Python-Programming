# a=5 #integer data type
# b=5.6 # float data type
# c="hello" #string data type

# d=a+b
# print(d)

# a=float(input("Enter the number a: "))
# print(a)

# a=float(input("Enter the float: "))
# print(a)
# b=int(a)
# print(b)

# print("hi"*5)
# print(" \t hi")
# print("\n \t hello")

# a=5
# b="hi"

# print(a)
# print(b)

# a,b=b,a
# print("\n")
# print(a)
# print(b)

# print((5+6)*2)
# a=8
# a-=1
# print(a)

# str1="hi"
# str2="hello"

# str1 += str2
# print(str1)

# b=10
# a=-b
# print(a)

#Write a program to calculate simple interest and compound interest.

# 1. Input the principal amount (principal)
# 2. Input the rate of interest (rate_of_interest)
# 3. Input the time period (time_period)
# 4. Calculate simple interest as (principal * rate_of_interest * time_period) / 100
# 5. Calculate compound interest as principal * (1 + rate_of_interest / 100) ** time_period - principal
# 6. Display the values of simple interest and compound interest

p=float(input("Enter the principal amount: "))
r=float(input("Enter rate of intrest: "))
t=float(input("Enter time period: "))
s_i=(p*r*t)/100
c_i=p*(1+r/100) ** t-p
print(r"Simple Intrest {s_i}")
print(r" Compound Intrest {c_i}")
