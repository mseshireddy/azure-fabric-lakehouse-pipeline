#print("Hello World")
#a = 10
#b = 10
#print('a',b)

#a,b = 10,10
#print(a,b)
#print('a',b)
#raju,ravi,hari = 15,12,18
#print(ravi)
#print('ravi')
#a=5
#print(a,'is of type', type(a))
#a=5.2
#print(a,'is of type', type(a))
#a=4+6j
#print(a,'is of type', type(a))
#s = 'Hello'
#print(type(s))
#s = 'Hello@123'
#print(s)
#print(type(s))
#s = '''Hello
#welcome to india'''
#print(type(s))

# find integer number types
#x = 5
#y = 2.5
#z = 1j

#type()

#print(type(x))
#print(type(y))
#print(type(z))

#Integer numbers is single or unlimited or negative or positive
#x = 1
#y = 22345678532755
#z = -3452894

#type()

#print(type(x))
#print(type(y))
#print(type(z))


#Float
# Float or "Floating point numbers" is a number, positive or nagative, 
# containing one or more decimal numbers

# Example:
#x = 1.10
#y = 1.0
#z = -35.59

#type()

#print(type(x))
#print(type(y))
#print(type(z))

# how to write power in python code mention "e" power in any number the type is float only
#x = 2e10
#y = 21e2
#z = -35.69

#type()

#print(type(x))
#print(type(y))
#print(type(z))

# complex numbers
# complex numbers are written with a "j" as the imaginary part
# example:
#x = 3+5j
#y=5j
#z=-5j

#type()

#print(type(x))
#print(type(y))
#print(type(z))

#Type conversion
#you can convert from one type to another with the int(),float(), and complex()
# method:
# Example:
#x = 1   #int
#y = 2.8 #float
#z = 1j  #complex
#print(type(x))
#print(type(y))
#print(type(z))



#convert from int to float
#a = float(x)

#convert from float to int
#b = int(y)

#convert from int to complex
#c = complex(x)
#print(type(a))
#print(type(b))
#print(type(c))


#Random Number
#python has a built in module called random that can be used to make randam numbers
#Example:
#import the random module, and dispaly a random number from 1 to 9:
import random
#print(random.randrange(1,10))

#another way to write

#a = random.randrange(1,10)
#print(a)

#what is string in python
# a string is a sequance of charecters.
#string can be created by enclosing charecters inside a single quota or double-quotes
#Triple quotes can be used represent multi line strings.
#string index sting indexing is forwar or backword  single charecter to print
#str = "Welcome to India"
#print(str[0])
#print(str[-16])
#slicing -  slicing means the one or more word or multiple charecters to print 
#print(str[0:7])
#print(str[0::2])
# if we want print reverse to do the reverse slicing method
#print(str[-1::-1])

#Key Points
#*input()
#*int()
#*float()
#*eval()

#a = input("Enter 1st Number:")
#print(a)
#print(type(a))
#b = input("Enter 2nd Number")
#print(a+b)
# it is side by side 1st and 2nd numbers is adding but it is wrong so correct this
#a = int(input("Enter 1st Number:"))
#b = int(input("Enter 2nd Number:"))
#print(a+b)

#Boolean Values
#Boolean values represent one of two values:True or False
# In programming you often need to know if an expression is true or false.
# you can evaluate any expression in python, and get one of two answers, True or False
# When you compare two values, Te expression is evaluated and python returns the boolean Answer
# Example:
#print(10 > 9) 
#print(10 == 9)
#print(10 < 9)

# print a message based on weather condition is True or False:
#a = 200
#b = 33

#if b > a:
#    print("b is grater than a")
#else:
#   print("b is not greater than a") 

#a = 300
#b = 500

#if b > a:
#    print("b is grater then a")
#else:
#    print("b is not grater then a")    

# python operaters
# operators are used to perform operations on varibles and values.
# in the example below, we use the + operator to add together two values
# Example:

#print(10+5) #print sum of 10 & 5, 15    

#python divides the operators in the following groups:
#Arithmatic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Bitwise Operators

# Arithmatix Operators
#Operator              Name                 Example
#  +                 Addition                x+y
#  -                 Substraction            x-y
#  *                 Multiplication          x*y
#  /                 Division                x/y
#  %                 Modulus                 x%y
#  **                Exponents               x**y
#  //                Floor Division          x//y
#Basic Arithamatic Operators
#a = 10
#b = 20
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

#Modulud Operator
#print(10%3)

#Exponent Operator
#print(2**3) # 2*2*2

#Floor Division
#print(16//3)

#Comparison Operators
# Operator               Name                     Example
# ==                     Equal                    x == y
# !=                    Not Equal                 x != y
#  >                    Grater than               x > y
#  <                    Less Than                 x < y
# >=                    Grater Than or Equal to   x >= y
#  <=                   Less than or Equal to     x <= y

#x = 20
#y = 10

#print(x == y)

#print (x!= y)

#print(x > y)

#print (x < y)

#print (x >= y)

#print (x <= y)

#Assignment Operators
# Operator             Example             Same As 
#  =                     x = 5              x =5
#  +=                    x+= 5              x = x + 3
#  -=                    x-= 3              x = x - 3

#x = 5
#x  = x + 5
#print(x)

#x += 5
#print(x)

#x = x - 5
#print(x)

#x -= 5
#print(x)

# Logical Operators
# it containes compare multiple conditions
# Operator         Description                                                    Example
#  and            Returns True If both statements are True                      x < 5 and x < 10
#  or             Returns True If one of the statement is True                  x < 5 or  x < 4
#  not            Reverse the results Returns False if the results is True      not(x<5 and x<10)

#x = 10
#y = 20

#print(x < y and y > x)

#print(x > y or y > x)

#print(not x > y)

#Identity Operators
# Operator                        Description                                      Example
# is             Returns True if both variables are the same Object                  x is y
# is not         Returns True if both variables are not the same Object              x is not y

#x = 10
#y = 10

#print(x is y, x==y)
#print(x is not y, x!=y)

# Membership Operators
#Operator     Description                                                               Example
# in      Returns True if a sequencewith the specified value is present in the object    x in y
# not in  Returns True if a sequencewith the specified value is present in the object    x not in y

#str = "Hello India"
#print('H' in str)
#print('h' in str)
#print('India' in str)

#print('us' not in str)

#Bitwise Operators
# Operator                    Name                   Example
# &                            AND                      x & y
# |                            OR                       x | y
# ^                            XOR                      x ^ y

#Bitwise Operators is truth tables(like binary values 0 1)
# Bitwise operators is works on binary numbers
# Truth Table 

# 1 : True         0  :  False
#  A            B            A&B           A|B          A^B
#  0            0             0             0            0 
#  0            1             0             1            1
#  1            0             0             1            1
#  1            1             1             1            0

#x = 10
#y = 8
#print(bin(x))
#print(bin(y))
#print(bin(x&y))
#print(bin(x|y))
#print(bin(x^y))     


#Conditional Statments or IF else Statements
#if [conditional Expression]:
#     [Statements (s) to execute]
# Example:

#a = 11
#if a%2==0:
#    print(a, "is even number")
#else:
#    print(a,"odd number")

#if elif else statement
#if [condition #1]
#           [statement #1]
#elif[condition #2]
#           [statement #2]
#elif[condition #3]
#           [statement #3]
# else
#            [statement when if and elif(s) are False]

#Example:
#marks = 55
#if marks >= 60:
#    print('First Class')
#elif marks >= 48:
#    print('Second Class')
#elif marks >= 35:
#    print('Third Class')
#else:
#    print('Fail')

#Python Calculator
# Assignment -1
#Calculator  Basic Programming Language
# Addition: +  Substraction: - Multiplication: *   Division: /

#num1 = int(input("enter 1st number:"))
#oper = input("enter the operator(+,-,*,/):")
#num2 = int(input("enter 2nd number:"))

# if oper == '+':
#     print(num1+num2)
# elif oper == '-':
#     print(num1-num2)
# elif oper == '*':
#     print(num1*num2)
# elif oper == '/':
#     print(num1/num2)

# else:
#     print('Invalid Operator')

#python For Loops
# A for loop is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set; or a string)
#Looping through a string 
# Even strings are iterable objects, they contain a sequenc of charecters:
#Example:
# Loop through the letters in the words "banana"
for x in "Banana":
    print(x)
range(5)
#start:0
#condition:n-1(5-1)
#increment:1

0,1,2,3,4

range(1,5)
#start:1
#condition:5-1
#increment:1

1,2,3,4

range(1,6,2)
#start:1
#condition:6-1
#increment:2

1,3,5
print(range(5))





