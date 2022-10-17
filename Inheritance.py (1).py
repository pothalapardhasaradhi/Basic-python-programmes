#!/usr/bin/env python
# coding: utf-8

# In[5]:


#To acess the attributes of one class from other class we can call it as inheritance
class Display:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("This is a constrctor method , whever we create object that time by default it's callable")
    def show(self):
        print("FIRST NAME:",self.fname)
        print("Last Name:",self.lname)
obh=Display("POTHALA","PARDHU")
obh.show()


# In[10]:


#Single level Inheritance: we can acess the attributes of one child class from one parent class
class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print("This is a constrctor method")
    def display(self):
        print("ID number:",self.id)
        print("Name:",self.name)
class Employee(Person):
    pass
obj=Employee("A855172","Pardhu")
obj.display()


# In[15]:


class Computer:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("This is a constrctor method")
    def Fun(self):
        print("The first computer is developed by",self.a)
        print("The release is happened in ",self.b)
class Laptop(Computer):
    pass
class Smartphone(Laptop):
    pass
obj=Smartphone("Charles babage",1991)
obj.Fun()


# In[42]:


class Pardhu:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def display(self):
        print("Emoployee Name:",self.a)
        print("Employee id:",self.b)
        print("Designation:",self.c)
        print("Salary:",self.d)
    def show():
        print("Hello welcome to python world!")
class Pavan:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def display1(self):
        print("Emoployee Name:",self.a)
        print("Employee id:",self.b)
        print("Designation:",self.c)
        print("Salary:",self.d)
    def show1():
        print("Hello welcome to python world!")
class Employee(Pardhu,Pavan):
    pass
obj=Pardhu("Pardhu","A855172","Developer",25000)
obj.display()
print("- - - - - - - - - - - - - - - - - - - - - - ")
obj1=Pavan("pavan","A855173","Tester",35000)
obj1.display1()
obj3=Employee("sai",103,"TL",10000)
obj3.display()
print("- -- - -- -- -- ---- --- --- --- -- -- -- - - -")
obj3.display1()
print("- -- - -- -- -- ---- --- --- --- -- -- -- - - -")


# In[44]:


class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
 
 
class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()


# In[51]:


class Person:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Professor(Person):
    def isProfessor(self):
        print(self.a,"is professor")
obj=Professor("pavan",34)
obj.isProfessor()


# In[61]:


class SuperClass1:
    num1=3
class SuperClass2:
    num2=5
class subclass(SuperClass1,SuperClass2):
    def fun(self):
        return self.num1+self.num2
obj=subclass()
print(obj.fun())
print(obj.num1)
print(obj.num2)


# In[68]:


class Parent:
    str1="POTHALA"
class Child:
    str2="PARDHASARADHI"
class grandChild(Parent,Child):
    def get(self):
        return self.str1+" " +self.str2
obj=grandChild()
obj.get()


# In[74]:


#Hierarchical inheritance
class sublclass:
    x=3
class subclass1(subclass):
    pass
class subclass2(subclass):
    pass
class subclass3(subclass):
    pass
obj=subclass()
obj1=subclass1()
obj2=subclass2()
obj3=subclass3()
print(obj.x,obj1.x,obj2.x,obj3.x)


# In[80]:


#hybrid inheritance
class A:
    a=10
class B:
    b="pardhu"
class C:
    c=[1,2,3,4]
class d(A,B):
    pass
obj=d()
print(obj.b)
print(obj.a)
obj=C()
print(obj.c)


# In[81]:


#Private attributes
"""sometimes we need to prevent the subclass from accessing certain attributes.

We can do this by prefixing the attribute name with double underscores. Subclasses can not access these attributes."""


# In[91]:


class Person:
    __name="Ashish" #private variables
class Employee(Person):
    def fun(self):
        return self.__name
obj=Employee() 
obj.fun() 


# In[96]:


#Method overloading: same method with different number of arguments
class Parent:
    def Hello():
        prinT("Hello Parent")
class Child:
    def Hello(a):
        print("Hello child")
class Pardhu(Parent,Child):
    pass
obj=Pardhu()
obj.Hello(3)


# In[98]:


#Method Overriding: same method with same number of arguments
class Parent:
    def fun(self):
        print("Hello python")
class Child(Parent):
    def fun(self):
        print("Hello Java")
obj=Child()
obj.fun()


# In[116]:


#his is used to access the parent class methods and attributes. 
#With the help of super(), we can also access the overridden methods.
class Parent:
    def info(self):
        print("This is all about python")
class Child(Parent):
    def info(self):
        print("This is all about java")
        super().info()
    def getParent(self):
        super().info()
obj=Child()
obj.info()
obj.getParent()


# In[124]:


#Constrctor invoked
class Student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class School(Student):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
obj=School("pardhu",101,25000)
print(obj.a,obj.b,obj.c)
        


# In[129]:


#Python built-in function. issubclass() returns True if the first
#argument is a subclass of the second argument, otherwise, returns False.
class Pavan:
    pass
class Pardhu(Pavan):
    pass
issubclass(Pardhu,Pavan)
issubclass(Pavan,Pardhu)


# In[130]:


#It returns True if the first argument is an instance of the second argument, otherwise, it returns False.
class ParentClass:
    pass
class ChildClass(ParentClass):
    pass
child = ChildClass()
print(isinstance(child, ChildClass))
print(isinstance(child, (ParentClass, ChildClass)))
#if we need to check whether the object is realted the particular class we can go far


# In[ ]:




