#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Check whether the number is even or odd
a=int(input("enter the number"))
if a%2==0:
    print(a," is even number")
else:
    print(a," is odd number")


# In[2]:


#Find out the largest of three numbers
a=int(input("enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
if a>b and a>c:
    print(a, " larger number")
elif b>a and b>c:
    print(b," is larger number")
else:
    print(c, " is larger number")


# In[5]:


#Check whether the number is positive or negative or zero
a=int(input("enter the numbr "))
if a<0:
    print(a," is negative number")
elif a==0:
    print(a," is zero")
else:
    print(a," is positive number")


# In[22]:


#Print the natural numbers from 1 to 10
a=int(input("enter the range of natural numbers"))
for i in range(1,a+1):
    print(i, end=" ")


# In[23]:


#Print the sum of n natural numbers in a particular range
a=int(input("Enter the starting number "))
b=int(input("Enter the ending number"))
sum=0
for i in range(a,b+1):
    sum=sum+i
print("the sum of natural number from",a," to", b,"is ",sum)


# In[24]:


#Find out the factorial of a number
a=int(input("enter a number "))
fact=1
if a<0:
    print(a," is Does not exists")
elif a==0:
    print("Factorial of a",a," 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("Factorial of a ",a," is",fact)


# In[26]:


#Check whether the person is eligible for voting or not(must 18 or morethan 18)
a=int(input("Enter your age"))
if a>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


# In[41]:


#Simple program on ATM system
import datetime
username="Pardhu123"
password="11111"
a=input("Enter username")
b=input("Enter passwprd")
amount=50000
if username==a and password==b:
    print("Login sucessfull")
    print("""====WELCOME TO SBI ATM=====
    1.Withdraw
    2.Deposit
    3.Balance check
    4.Mini statement
    5.exit""")
    c=int(input("choose option based on numeric value"))
    
    if c==1:
        d=int(input("Enter the amount to be withdraw"))
        if amount>d:
            amount=amount-d
            print("The Current balance is", amount)
        else:
            print("Insufficient funds")
    elif c==2:
        d=int(input("Enter the amount to be deposit"))
        amount=amount+d
        print("The current balance is ",amount)
    elif c==3:
        print("The available balance is ",amount)
    elif c==4:
        print("======MINI STATEMENT========")
        print("Username:",username)
        print("The available balance", amount)
        print("The current date and time is",datetime.datetime.now())
        print("==========THank YOU+========")
    else:
        print("Exit")
print("Thank you for visiting us",username)
print("Have a nice day")

        
        


# In[42]:


#To print a table
a=int(input("Enter the table number you want"))
for i in range(1,11):
    print(a,"X",i,"=",a*i)


# In[44]:


#Check whether the string is palindrome or not
a=input("Enter the string")
if a==a[::-1]:
    print(a," is palindrome")
else:
    print(a, " is not a palindrome")


# In[ ]:




