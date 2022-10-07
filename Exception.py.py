#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""3 types errors
1.syntax error(compiler error)
2.logical error()
3.run time eeror"""
for i in range(10)
print(i)


# In[3]:


a,b=10,20
c=a-b
print(c)
#logical error


# In[4]:


#runtime error
a=int(input())
b=int(input())
print(a/b)
#exceptions are nothing but a errors that appear in while running the programm


# In[6]:


a=int(input("Enter a numner"))
b=int(input("Enter a number"))
try:
    c=a/b
    print(c)
except:
    print("Exception raised")
else:
    print("No exception ")
finally:
    print("By default executed")


# In[7]:


#How to handle single exceptrion 
a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except:
    print("Exception raised")


# In[9]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except Exception as e:
    print(e)


# In[11]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except :
    print("Exception raised so using default value for denominator")
    b=1
    c=a/b
    print(c)


# In[12]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except ZeroDivisionError:
    print("Exception raised")


# In[13]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except IndexError:
    print("Exception raised")


# In[15]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
l=[10,20,30,40,50]
try:
    c=a/b
    print(c)
    print(l[5])
except ZeroDivisionError:
    print("Exception raised")


# In[1]:


#How to handle multiple Exceptions
a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))
l=[10,20,30,40,50]
try:
    d="python"+19
    c=a/b
    
    print(l[5])
except ZeroDivisionError:
    print("Dividing by zero exception has raised")
except IndexError:
    print("Index out of range ")
except:
    print("Exception error")
#Multiple exceptions handled by multiple extension blocks


# In[6]:


a=int(input("enter anumber"))
b=int(input("enter a number"))
try:
    c=a+b
    print(c)
    d=a/b
    print(d)
except ValueError:
    print("Error raised bro")


# In[8]:


a=int(input())
b=int(input())
l=[1,2]
try:
    c=a/b
    print(c)
    print(l[5])
except(ZeroDivisionError,IndexError):
    print("Exception raised")


# In[12]:


#valueError
import math
a=int(input("Enter a number "))
try:
    print("the square root of a is",math.sqrt(a))
except ValueError:
    print("Exception Error")
#we need to enter positive value


# In[17]:


#TypeError
a=int(input())
b=int(input())
try:
    c=a/b
except TypeError:
    print("Exception raised")


# In[19]:


#raise exception are used to validate the inputs
a=int(input("enter a value"))
b=int(input("Enter b value"))
try:
    if b==0:
        raise Exception("Divides by zero")
    c=a/b
    print(c)
except:
    print("Exception raised")


# In[22]:


a=int(input("Value foe a"))
b=int(input("Value of b"))
try:
    if b==0:
        raise Exception("Exception raised")
    c=a/b
    print(c)
    
except Exception as e:
    print(e)


# In[25]:


marks=int(input("Enter marks"))
try:
    if marks<0 or marks>100:
        raise Exception("Marks should be in between a and 100")
    print(marks)
except Exception as e:
    print(e)


# 
