"""variables"""

# sher = "harsh bhaiya"

# SheryiansSchool = "students" #pascal case

# sheryiansSchool = "students" #camel case

# sheryians_school = "students" #snake case




"""data types"""

# a = -34

# b = 56.8
# c = 12/3

# v = 34j

# print(type(c))



# st = '1231243235 dsagaiogiaeb !@#$%^&*'

# print(type(st))

# b = True

# t = False

# print(type(b))


"""strings"""

# a = "SHER CODER"


# print(a[::])

'''type conversion'''

# a = 12/3
# a = str(a)
# print(type(a))

# a = 0 
# print(bool(a))

# falsy strings - (false , 0.0 , 0 , "" , [] , () , {} ) seven strings which always give false in bool type 

# implict conversion - 
# a = 12 
# print(a/2)

# explicit conversion - 
# a = 12/2
# print(type(a))

# name = "harsh"
# age = "19"

# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age"))

# print(f"my age is {age}")

# height = int(input("what is your height"))
# print(f"my height is {height} feet")

"""Operators"""

# a = 5
# b = 32


# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)( it will be directly converts the output into integer )
# print(b/a)( and here the ans wil be in float )
# print(5**2)(it means 5 ki power 2 ,  ** is used as exponent power )
# print(32%5)(this is used to find out the remainder)

# print(12+4/2) (python also follows bodmass rule)


#assignment operators (used to assign values to the operators)

# a = 23

#compound assignmet operations

# a = 20
# a = a+20(reassigning values)
# print(a)

# a = 20 
# a += 20. (another way to assign the value)
# a += 40
# a += 60
# a-=
# a*=
# a/= 2
# a//= 2
# a**= 2

# print(a)

"""Comparision operators"""
# (always provide boolean output(true or false ))
# (there are 6 types of comparison operations > , > , >= , <= , == , != )
"""integer comparison"""
# a = 12.1
# b = 12 

# print(a == b)

# print(a != b) ( it means a is not equal to b )
# print(a > b)
# print(45 < 67)
# print(23 >= 23) 
# print(45 <= 45)
# ( here the ans will be in true and false only )
"""string comparision"""

# (strings are compared on the basis of there ascii values)
# print(ord("A"))(this is the method to find out the ascii value of string)
# print(ord("B"))
# print("A">"B")
 
# print("ABC" > "ACD")(in this we have to compare first letters first then next letters ascii values left to right)

# print("A" > 34) ( we cannot compare a string with an integer )

"""Logical operators"""
# there are 3 types of logical operators
# (and , or , not )

# and = return true if all conditions are true , if at least one is false then the complete output will be false
# Or = return true if  atleast one is true  , it will give false only when all are false 
# not = reverses the boolean values 

# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

# print(not 12 == 12) ("not" logical operator)

"""conditional statements"""
#IF else 

# a = 6

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")

# ------------elif example ----------------------

# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")

# else:
#     print("Unidentified gender")

# -------------Even odd problem-----------------

# num = int(input("please tell your number :- "))

# if num%2 == 0: 
#     print("even number")

# else:
#     print("Odd number")

# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")

# -----------------valid voter problem-----------------------

# age = int(input("your age = "))
# if age >= 18 :
#     print("you are a valid voter")
# else:
#     number_of_years_remaining_to_vote =(18-age)
#     print(f"number of years to become a valid voter:{number_of_years_remaining_to_vote}")

# ----------------leap year problem -------------------------
# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")

# -----------------ifelif leadder ----------------------------

# t = int(input("please tell the temprature :- "))

# if t < 0:
#     print("Freezing cold")

# elif t >= 0 and t <10:
#     print("very cold")

# elif t >= 10 and t <20:
#     print("cold")

# elif t >= 20 and t <30:
#     print("plesant")

# elif t >= 30 and t <40:
#     print("hot")

# else:
#     print("temprature is very hot ")


# print("hello world ")

"""LOOPS"""
# Loops are powerful constructs in python that allows you to execute a block of code multiple times .By understanding and using for and while loops, along with loop conttrol statements like break, continue, and pass, you can handle a wide range of programming tasks efficiently.

#For loop

# range(s,s,s)(start, stop , steps)

# a = range(1,100)
# for i in a:
#     print(i)

#---------------Table Problem-------------------------------

#lets print a table of 5
# n = int(input("Which table you want ? "))
 
# for i in range(n,(n*10)+1,n):
#     print(i)

#----------------Loops in strings---------------------------

# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         break
#     else: 
#        print(i)-------(it will break on 15 and continue to 20)

# for i in range(1,21):
#     if i == 15 :
#         continue
    # print(i)-------------(it will skip 15 and write all the values from 1 to 20)

# for i in range(1,21):
#     if i == 15:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")-------# (pehle if stament run hua orr break nahi hua to hi else statement use hoga and last wala print hojayega )

"""For Loop Questions"""

# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world ")

# n = int(input("please tell your number ")) 

# for i in range(1,n+1):
#     print(i)

# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)

#-------------Another way to represent a table---------------------

# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#-------------sum of numbers upto a particular number--------------

# n = int(input("please tell your number:- "))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")

#(similarly factorial of number can be calculated by useing fact at place of sum )
#(and initially we can't take fact 0 , it will give 0)
# n = int(input("please tell your number:- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i


# print(f"your factorial is {fact}")

#---------------------odd even sum problem------------------------

# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")

#-----------------printing factor problems-------------------------

# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

#--------------------perfect number problem-------------------------
            
# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")

#-------------------Prime numbers btw (1,100)--------------------------

# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)    

#-------------------prime number problem----------------------------- 

# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#--------------------reverse using for loop---------------------------

# a = "SHERYIANS"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

#----------------------palindrome problem------------------------------

# a = "NAMAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")


# ------------counting diffrent types of charecters in strings -----------

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))----(this will print all the directories in string)

"""WHILE LOOP QUESTIONS"""

# ------------seperating each number each in a new line-----------------

# a = 256

# while a >0 :
#     print(a % 10)
#     a = a // 10


# a = 1 

# while a <= 30:
#     print(a)
#     a = a + 1

#-------------reversing using while loop ----------------------------

# a = int(input("tell your number"))

# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# print(rev)

#-------------pallindrome problem using whle loop -------------------

# a = int(input("tell your number"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")

"""Random library"""

#--------------counting tries during number guess---------------------

# import random
# print(random.randint(1,10))
# a = ["anurag","harsh","om","lmbaa","lugai"]
# print(random.choices(a))

# num = random.randint(1,10) 

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 :- "))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number in {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries +=1
    
#     elif num > guess:
#         print("go a little higher")
#         tries +=1

#     else:
#         tries +=1 
#         print("sorry you are wrong")

"""FUNCTIONS"""
# It is a block of reusable code , that we create and whenever we want to use it , we can call it .

# print(12)


# def hello():
#     print("this is a hello function so I a m doing hello")


# hello()


# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22,name = "akarsh")

#"naman"
# def pallindrome(st = "NAMAN"):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
    
#     if rev == st:
#         return True
#     else:
#         return False



# print(pallindrome())
# pallindrome("CURSOR")

# def hello():
#     return "hello how are you"

# print(hello())

"""""""""""""""""""""""""Data structures"""""""""""""""""""""""""

'''Key Words'''
    # 1.Mutable - mutability refers to whether an objects value can be changed after creation. And list allow this.
    # 2.Duplicates - we know data structures are used to store multiple value so duplicates means same value occuring multiple time. List allows this.
    # 3.Ordered - List maintains ordered data structures maintains the sequence of elements as they were inserted. This means you can access elements using their position(index).
    # 4.Heterogenous - list have heterogenous nature that means we can have multiple data types inside the list. 

'''LIST'''
# a = [12,13,14,15,16,34.5]

# a = ["a",1,[1,3],True]
# print(a[2][0])

# Loop in LISTS - 

# #1st way using index
# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values
# for i in a:
#     print(i)

# print(dir(list)) - this gives the methods performed in list.
# help(list) - this is used to learn about any method.

'''Methods in list'''
# a=[1,2,4,3]
# b=[3,4]
# a.extend(b) - it is used to extend a list with another list.
# print(a)
# a.append(3) - it will add 3 in last of the list.
# print(a)
# a.pop("index of number") - it is used to remove the number from list whose index you are giving.
# print(a)
# a.insert(2,4) - it will add "4" on 2nd index.
# print(a)
# a.remove(3) - it is used to remove the first "3" in list.
# print(a)
# a.sort() - sort the list in ascending order.
# print(a)
# b = a.index(6) - it will tell the index of number "6" in the list.
# print(b)
# b = a.count(5) - it will find the count of number "5" that how much time "5" is occuring in list.
# print(b)
# a.reverse() - it will reverse the list order.
# b = a.copy() - it will create a copy of the list.
# a =""
# b=bool(a)
# print(b)

'''''''''''''''Questions'''''''''''''''

# --------------Finding positive and negative numbers------------

# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("negitive elements are")

# for i in l:
#     if i < 0:
#         print(i)

#-----------------Finding Mean of List----------------------

# l = [12,435,67,89,23,25,69]
# s = len(l)
# print(s)
# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))

# --------------------Findiing largest number---------------

# l = [12,567,43,235,347,568,45,7]
# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")

# --------------Finding second largest number----------------
# l = [1,16,17,15,19,18]
# def findsecondlargestandlargest(l):
#     sec_largest = l[0]
#     largest = l[0]
#     for i in l:
#         if i > largest:
#             sec_largest = largest
#             largest = i
#         elif i > sec_largest:
#             sec_largest = i
#     return largest , sec_largest

 
# print(findsecondlargestandlargest([1,6,0,7,4,8,9,10]))

#-------------checking if list is sorted---------------
# a = [12,13,18,15,16]

# for i in range(len(a)-1): 
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

"""Tuple"""

# a = (1,2,3,4,5,5,5.5,print(),"hello")

# count = a.count(5)
# print(count)


# a = (1,)

# print(type(a))



# a = {1,8,9,"hello",2,3,4,5}

# for i in a:
#     print(i)

# a = {8,1,2,3,4}

# a.clear()

# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# b -= a

# print(b)

# d = {10:100,20:200,30:300,40:400}

# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 

# print(d)




# d = {10:100,20:200,30:300,40:400}

# print(d.items())

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# d1 = {10:100,20:200,40:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)


# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1

# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]



# a = int(input("tell your number :- "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")




# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")

#File handling

# r = open("superman.txt",'a')

# r.write("and now I am appending some content inside the file  ")

# r.close()

# class Factory:
#     a = 12 # attribute 

#     def hello(self): #method
#         print("how are you")
    


# obj = Factory()

# obj2 = Factory()


# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"your object details are {self.material}, {self.pockets},{self.zips} ")
    


# reebok = Factory("leather",3,2)

# campus = Factory("nylon",3,3)

# reebok.show()

   

# class Animal:
#     name = "lion" #class attribute
    
#     def __init__(self,age):
#         self.age = age #instance attribute
    
#     def show(self):  #instance method
#         print(f"how are you your agger is {self.age}")
    
#     @classmethod
#     def hello(cls):
#         print(f"how are you brother {cls.age}")

#     @staticmethod
#     def static():
#         print("how are you")

   

# obj = Animal(12)

# class Factorymumbai: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class /subclass
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")
    

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")


# animal1 = Animal("lion")
# person1 = Human("akarsh",23)

# animal1.show()


# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human,Animal):
#     name3 = "charli123"

# obj = Robots()

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips 
    

# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
    
# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# class Animal:
#     def show(self):
#         print("hello I am akarsh")
    


# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show()


# class Animal:
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()

# obj.show()


# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion",12)
# obj2 = Animal("dolphin",14)
# obj3 = Animal("tiger",34)

# print(obj + (obj2,obj3))


# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
    
# obj = Animal()

# obj.show



# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


# def information(**kwargs):
#     print("your information is\n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    



# information(name = "Akarsh", age = 23, designation = "AI/ML")

# l = {i : i**2 for i in range(1,10)}

# print(l)

# a = [1,2,3,4,5]

# def double(x):
#     return x *2

# result = map(double,a)

# print(list(result))

# from modelss.model import hello,maths

# a = int(input("how many rows you  want "))

# for i in range(1,a + 1):
#     for j in range(i):
#         print("* ",end = "")
#     print()

# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()



# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()

# a = 1234
# copy = a
# sum = 0

# while a > 0:
#     z = a %10
#     fact = 1 
#     for i in range(1,z+1):
#         fact = fact * i
    
#     sum = sum + fact
#     a = a//10 

# if sum == copy:
#     print("this is a strong number ")
# else:
#     print("not a strong number")


# for j in range(2,21):
#     a = j

#     for i in range(2,(a//2)+1):
#         if a % i == 0:
#             break

#     else:
#         print(a)



# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count = 0
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] +=1 
#     else:
#         dict[i] = 1
# max = 0
# for i in dict.values():
#     if i > max:
#         max = i
# for i in dict:
#     if dict[i] == max:
#         print(f"{i} occured {max} times and that is largest occurence")
#         break




"""""""""""""""""""""""""""""DSA"""""""""""""""""""""""""""

# -----------------Divisiblity of numbers----------------------

# class solution:
#     def fizzbuzz(self, n:int) ->list(str):
#         ans = []
#         for i in range(1,n+1):
#             if i%3 == 0 and i%5 == 0:
#                 ans.append("FizzBuzz")
#             elif i%3==0:
#                 ans.append("Fizz")
#             elif i%5==0:
#                 ans.append("Buzz")
#             else:
#                  ans.append(str(i))

#         return ans
    

# --------------Count Odd numbers in an interval----------------

# class solution:
#     def countodds(self, low:int, high:int) -> int:
#         return (high+1)//2 - (low)//2


#--------How many numbers are smaller than current number------

# class solution:
#     def smallernumbersthancurrent(self, nums:List[int]) ->[int]:
#         ans = [0]*len()
#         for i in nums:
#             for j in nums:
#                 if j < 1:
#                     c+=1
#             ans.append(c)  

#         return ans         


#-----------Count digits that divide a number---------------

# class solution:
#     def countdigits(self, num: int) -> int:
#         temp = num
#         ans = 0
#         while temp>0:
#             r = temp%10
#             if num%r == 0:
#                 ans +=1
#             temp=10
#         return ans



"""""""""""''''''''DSA Questions'''''"""""""""""""""

# 🔥 SECTION-WISE IMPORTANT CODING QUESTIONS (WITH SOLUTIONS)




# 1️⃣ PREFIX SUM & TWO POINTERS (VERY HIGH WEIGHT)

# ✅ Q1. Running Sum of 1D Array

# Problem:
# Given an array, return its running sum.

# arr = list(map(int, input().split()))

# res = []
# curr = 0
# for x in arr:
#     curr += x
#     res.append(curr)

# print(res)


# ---

# ✅ Q2. Subarray Sum Equals K ⭐⭐⭐

# Problem:
# Find number of subarrays with sum = k.

# arr = list(map(int, input().split()))
# k = int(input())

# prefix = 0
# count = 0
# mp = {0: 1}

# for x in arr:
#     prefix += x
#     if prefix - k in mp:
#         count += mp[prefix - k]
#     mp[prefix] = mp.get(prefix, 0) + 1

# print(count)


# ---

# ✅ Q3. Best Time to Buy and Sell Stock

# prices = list(map(int, input().split()))

# min_price = prices[0]
# profit = 0

# for p in prices:
#     min_price = min(min_price, p)
#     profit = max(profit, p - min_price)

# print(profit)


# ---

# ✅ Q4. Two Sum II (Sorted Array)

# arr = list(map(int, input().split()))
# target = int(input())

# l, r = 0, len(arr)-1
# while l < r:
#     s = arr[l] + arr[r]
#     if s == target:
#         print(l+1, r+1)
#         break
#     elif s < target:
#         l += 1
#     else:
#         r -= 1


# ---

# ✅ Q5. Remove Duplicates from Sorted Array

# arr = list(map(int, input().split()))

# k = 1
# for i in range(1, len(arr)):
#     if arr[i] != arr[i-1]:
#         arr[k] = arr[i]
#         k += 1

# print(k)
# print(arr[:k])


# ---

# 2️⃣ STRING ALGORITHMS (GUARANTEED THEORY + CODE)

# ✅ Q6. Check Substring

# s = input()
# sub = input()

# print(sub in s)


# ---

# ✅ Q7. Subsequence Check

# s = input()
# t = input()

# i = j = 0
# while i < len(s) and j < len(t):
#     if s[i] == t[j]:
#         j += 1
#     i += 1

# print(j == len(t))


# ---

# ✅ Q8. Common String Methods (IMPORTANT)

# s = "hello world"
# print(s.split())
# print(" ".join(["a","b"]))
# print(s.find("o"))
# print(s.replace("world", "python"))
# print(s.rfind("o"))


# ---

# 3️⃣ KADANE’S ALGORITHM ⭐⭐⭐ (100% COMING)

# ✅ Q9. Maximum Subarray Sum

# arr = list(map(int, input().split()))

# max_sum = curr = arr[0]
# for i in range(1, len(arr)):
#     curr = max(arr[i], curr + arr[i])
#     max_sum = max(max_sum, curr)

# print(max_sum)

# Time Complexity: O(n)


# ---

# 4️⃣ SORTING ALGORITHMS (DRY RUN FOCUS)

# ✅ Q10. Bubble Sort

# arr = list(map(int, input().split()))

# n = len(arr)
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)


# ---

# ✅ Q11. Insertion Sort

# arr = list(map(int, input().split()))

# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key

# print(arr)


# ---

# ✅ Q12. Selection Sort

# arr = list(map(int, input().split()))

# for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# print(arr)


# ---

# 5️⃣ BINARY SEARCH & VARIATIONS ⭐⭐⭐

# ✅ Q13. Search Insert Position

# arr = list(map(int, input().split()))
# x = int(input())

# l, r = 0, len(arr)-1
# ans = len(arr)

# while l <= r:
#     mid = (l+r)//2
#     if arr[mid] >= x:
#         ans = mid
#         r = mid - 1
#     else:
#         l = mid + 1

# print(ans)


# ---

# ✅ Q14. Square Root of X

# x = int(input())

# l, r = 0, x
# ans = 0
# while l <= r:
#     mid = (l+r)//2
#     if mid*mid <= x:
#         ans = mid
#         l = mid + 1
#     else:
#         r = mid - 1

# print(ans)


# ---

# ✅ Q15. Search in Rotated Sorted Array

# arr = list(map(int, input().split()))
# target = int(input())

# l, r = 0, len(arr)-1
# while l <= r:
#     mid = (l+r)//2
#     if arr[mid] == target:
#         print(mid)
#         break
#     if arr[l] <= arr[mid]:
#         if arr[l] <= target < arr[mid]:
#             r = mid - 1
#         else:
#             l = mid + 1
#     else:
#         if arr[mid] < target <= arr[r]:
#             l = mid + 1
#         else:
#             r = mid - 1


# ---

# 6️⃣ ARRAY MANIPULATION

# ✅ Q16. Minimum Swaps to Sort Array

# arr = list(map(int, input().split()))

# n = len(arr)
# arrpos = list(enumerate(arr))
# arrpos.sort(key=lambda x: x[1])

# visited = [False]*n
# swaps = 0

# for i in range(n):
#     if visited[i] or arrpos[i][0] == i:
#         continue
#     cycle = 0
#     j = i
#     while not visited[j]:
#         visited[j] = True
#         j = arrpos[j][0]
#         cycle += 1
#     swaps += cycle - 1

# print(swaps)


# ---

# 7️⃣ LINKED LIST (VERY IMPORTANT)

# ✅ Q17. Find Middle of Linked List

# slow = fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

# print(slow.data)


# ---

# ✅ Q18. Detect Cycle in Linked List

# slow = fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#         print("Cycle")
#         break
# else:
#     print("No Cycle")


# ---

# 8️⃣ HASHING (DICTIONARY & SET)

# ✅ Q19. Frequency using Dictionary

# arr = list(map(int, input().split()))
# freq = {}

# for x in arr:
#     freq[x] = freq.get(x, 0) + 1

# print(freq)

#---

# ✅ Q20. Use Set to Remove Duplicates

# arr = list(map(int, input().split()))
# print(list(set(arr)))

# --------------------TWO POINTER-------------------------

# arr = [1,2,3,4,5,6]
# target = 7
# m = 0
# n = len(arr)-1
# while m < n:
#     sum = arr[m] + arr[n]
#     if (sum == target):
#         print([m+1,n+1])
#         break
#     if sum < target:
#         m += 1
#     else:
#         n-=1

#----------------------KEDDENS ALGORITHIM------------------

# current_sum = nums[0]
# max_sum = nums[0]
#      for i in range(1,len(nums)):
#         current_sum = max(nums[i],current_sum + nums[i])
#         max_sum = max(max_sum , current_sum)
#      return max_sum

#--------------------Linear search---------------------
# arr = [1 , 3, 4, 5, 6 ]
# def search(arr , nums):
#     for i in range(len(arr)):
#         if arr[i] == nums:
#             return i
#     return -1
# print(search(arr , 7))

#-----------------Binary search--------------------------

# arr = [1, 3, 4, 5, 6, 7]
# low = 0
# high = len(arr) - 1
# target = 6

# while low <= high:
#     mid = (low + high) // 2
    
#     if arr[mid] == target:
#         print(mid)
#         break   # ✅ stop the loop
#     elif target < arr[mid]:
#         high = mid - 1
#     else:
#         low = mid + 1


#----------------------SORTING----------------------------
#BUBBLE SORT

# arr = [1,6,3,7,0,2,4]
# for i in range (len(arr)):
#     for j in range (1 ,len(arr)-i):
#       if arr[j] < arr[j - 1]:
#          arr[j],arr[j-1] = arr[j -1],arr[j]
# print(arr)

# a = [1,2,3]
# a[0]=3
# print(a)
# t = (1,23)
# t[1]=2
# print(t)
# t = ("a",1,True,(1,2),[1,2])
# print(t[3][0])

# a,b = (1,2)
# print(a,b)
# c = (91,2,3,4,5,6,7,8)
# a,d,b,e,f,g,h,i = c
# # a,b,d,*args = c
# print(a,d,b,e,f,g,h,i)

# a = "anurag"
# b = a.count("a")
# a = 2,3,4,6,2
# # b=a.count(2)
# print(b)
# # print(a,type(a))
# b = a.index(3)
# print(b)


# a = {"anurag":"a",2:"b"}
# a.pop()
# # a["anurag"]="Singh"
# # a["Harsh"]="om"
# # b=a.keys()
# # c=a.values()
# # d=a.items()
# # print(d)
# # print(a[1])
# print(a)

# my_dict = {'apple': 'red', 'banana': 'yellow'}

# # Example with existing key
# print(my_dict.get('apple'))

# # Example with missing key (returns None by default)
# print(my_dict.get('grape'))

# # Example with missing key and a specified default value
# print(my_dict.get('grape', 'purple'))
# print(my_dict)

# for v in my_dict.values():
#     print(v)

# s = {1,2,3,4}
# s = {1,2,2,3,4,5,5}
# s.add(10)
# s.remove(10)
# d = s.discard(12)
# print(d)
# c={}
# d = set()
# print(type(d))
# d = [2,4,4,4,4,4]
# c=set(d)
# print(c)
# a=s.pop()
# print(a)
# print(s)
# s.add(a)
# print(s)

# s={1,2}
# d={2,4}
# print(s|d)
# print(s.union(d))
# print(d&s)
# print(d.intersection(s))
# print(d-s)

# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}

# # Using the symmetric_difference() method
# result_method = set_a.symmetric_difference(set_b)
# print(f"Symmetric difference using method: {result_method}")

# # Using the ^ operator
# result_operator = set_a ^ set_b
# print(f"Symmetric difference using operator: {result_operator}")

# # Using symmetric_difference_update() (modifies set_a in-place)
# set_a.symmetric_difference_update(set_b)
# print(f"Set A after update: {set_a}")
