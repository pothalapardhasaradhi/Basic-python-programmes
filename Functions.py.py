#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Perform Arithematic OPerations
def Math(a,b):
    print("Addition of two numbers ",a+b)
    print("Substraction of two numbers ",a-b)
    print("Multiplication of two numbers ",a*b)
    print("Division of two numbers a/b ",a/b)
Math(2580,2580) #positional or required arguments


# In[5]:


#required arguments means :number of arguments should be same in both fuction call and function definition
def dispaly(name,age):
    print(name)
    print(age)
display("Pardhu",24)


# In[6]:


#optiona or default:number of arguments need not be match fcall and f definition
def display(name,age=56):
    print(name)
    print(age)
display("pspk")


# In[8]:


def math(a=0,b=1):
    print("Value of a is:",a)
    print("value of b is:",b)
    print(a+b)
    print(a-b)
    print(a*b)
math(2,5)
math()


# In[11]:


#variable number of arguments: are used to pass variable number of arguments to a function. syntax *
def fun(*args):
   print(type(args))
   print(args)
fun(1,2,3)
fun(1)
fun([1,2,3,45])
   


# In[13]:


def fun(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
fun(1,2,3,45,8)


# In[17]:


#kwargs stands for keyword arguments, it pass the data in the form of dictionary
def fun(**kwargs):
    print(type(kwargs))
    print(kwargs)
fun()


# In[20]:


#Write a python fuction that acepts a string and calclate the number of upper and lower letters 
def fun(str):
    a=0
    b=0
    s=0
    for i in str:
        if i>='a' and i<='z':
            a=a+1
        elif i>='A' and i<='Z':
            b=b+1
        elif i==" ":
            s=s+1
    print("Lower",a)
    print("Upper",b)
    print("spaces",s)
    print(a+b+s,"must equal",len(str))
fun("pardhu SARADhi HELlo ")


# In[22]:


#Write a python function that takes a list and returns a new list with unique elements of first list without using set
def unique(a):
    b=[]
    c=[]
    for i in range(a):
        i=int(input("Enter a value adding into list"))
        b.append(i)
        for j in b:
            if j not in c:
                c.append(j)
    print(c)
                
        
unique(5)


# In[24]:


#Prime or not
def fun(a):
    for i in range(2,a):
        if a%2==0:
            break
    else:
        print(a,"is prime number")
fun(2)


# In[27]:


#Palindrome or not
def fun(a):
    if a==a[::-1]:
        print("palindrome")
    else:
        print("Not palindrome")
fun("123")


# In[28]:


#REmove all occurances in agiven list
def fun(a):
    a.clear()
    print(a)
fun([1,2,3,4,5])


# In[31]:


#Write a python program that takes a list of words and return the length of longest one
def fun(a):
    b=len(a[0])
    c=a[0]
    for i in a:
        if len(i)>b:
            b=len(i)
            c=i
    print(b,c)
fun(["pspj","dfghjkl","sdrtyuiohgfd"])          
        


# In[32]:


#sum of first n natural numbers
def fun(a):
    sum=0
    for i in range(a):
        sum=sum+i
    print("The sum of first n natural numbers is", sum)
fun(10)


# In[33]:


#Write a pthon program that will return true,if the given two integers values are equal or their sum  or difference is 5
def fun(a,b):
    if a==b:
        print("True")
    elif a+b==5 or a-b==5:
        print("True")
    else:
        print("False")
fun(10,5)


# In[38]:


#Print prime numbers in a particular range
def fun(a,b):
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,"is prime number")
fun(5,100)
        


# In[42]:


#Fibonacci series
def fib(a):
    a=0
    b=1
    i=0
    while a>i:
        print(a,end=" ")
        temp=a+b
        b=a
        a=temp
        i=i+1
fib(10)


# In[49]:


#factorial of a number
def fact(a):
    a=1
    for i in range(1,a+1):
        a=a*i
    print(a)
fact(0)


# In[ ]:




