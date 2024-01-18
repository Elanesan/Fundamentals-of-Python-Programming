# n=int(input("Enter the number: "))
# if n==0:
#     fact=1
# fact=1
# for i in range(1,n+1):
#     fact=fact*i  
# print(f"The fact of {n} is {fact}")      

# n=int(input("Enter n: "))
# iscomposite=0
# for i in range(2,n):
#     if (n%i==0):
#         iscomposite=1
#         break
# if (iscomposite==1):
#     print("num is composite")
# else:
#     print("Prime")    

# def remove_v(s):
#     new_str=" "
#     for i in "aeiouAEIOU":
#         pass
#     else:
#         new_str +=i
#     print("After remove: ",new_str)
# str=input("\n Enter the string: ")
# remove_v(str)  

# def palin(s):
#     return s==s[::-1]
# s="hello"
# ans=palin(s)
# if ans:
#     print("Palindrome")
# else:
#     print("not")          

# odd=[2*i +1 for i in range(20)]
# print(odd)

# def is_even(n):
#     return n%2==0
# num=[3,2,4,6,7,9,13,590,7647647,986875]
# even=list(filter(is_even,num))
# print(even)  

# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()          

# def lin_s(list,n,x):
#     for i in range(0,n):
#         # print(i)
#         if list[i]==x:
#             return i
        
# list=[1,2,3,4,5,6,7,8,9,10,11]
# x=7
# n=len(list)
# result=lin_s(list,n,x)
# print(f"found at {result}")  

# nested=[[1,2,3],[4,5,6],[7,8,9]]   

# for row in nested:
#     for column in row:
#         print(column,end=' ')  
#     print()             

def foo(x,y):
    return x+y
result=foo(3,foo(2,1))
print(result)    
