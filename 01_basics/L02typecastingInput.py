# ''' scenario 1'''
# a=1
# b=2
# print(a+b) # output - 1+2=3 bcz 1 & 2 => int

# ''' scenario 2'''
# a=input()  #let input be 1
# b=input()  #let input be 2
# print(a+b) #output - 1+2=12 bcz input by default string value hoti hai so=> "1"+"2" = "12"
# #to overcome this refer 3rd scenario-

# ''' scenario 3'''
# a=int(input())  #let input be 1
# b=int(input())  #let input be 2
# print(a+b)      # output- 1+2=3 bcz typecasted string into int

'''__________________________________________________________________________________________________________________________________________________________________
Typecasting in python:
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
Two Types of Typecasting:
Explicit Conversion (Explicit type casting in python)
Implicit Conversion (Implicit type casting in python)

Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer or manually as per the requirement.
It can be achieved with the help of Python's built-in type conversion functions such as :
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. 
Example:                                                                                                                                   
string_naam = "15"
number = 7
string_number = int(string_naam) #throws an error if the string_naam is not a valid integer mtlb if string_name="hi" toh isko toh int m convert nhi kr skte na
sum = number + string_number
print("The Sum of both the numbers is: ", sum)                                                                                          
Output:
The Sum of both the numbers is 22

Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. 
Some of the data types have higher-order, and some have lower order. 
While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type.
According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
Python converts a smaller data type to a higher data type to prevent data loss. 
Example of implicit type casting:                                                                                                      '''                                                                                                   
# Python automatically converts
# a(int) to float for addition with b (float)
a = 7
print(type(a))
 
#bcz b is float (higher-order)
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Ouput of above:
# <class 'int'>
# <class 'float'>
# 10.0
# <class 'float'>





