'''
Python Functions:
A function is a block of code that performs a specific task whenever it is called.
There are two types of functions:
Built-in functions
User-defined functions

* Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

* User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
Syntax:
def function_name(parameters):
  #indentation matters here too!
  # Code and Statements

_________________________________________________________________________________________________________________________________
Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

Example:
#defining a function
def name(fname, lname):
    print("Hello,", fname, lname)

#calling a function
name("Sam", "Wilson")

Output:
Hello, Sam Wilson 
__________________________________________________________________________________________________________________________________________
Function Arguments & return statement:
There are four types of arguments that we can provide in a function:
i)Default Arguments
ii)Keyword Arguments
iii)Variable length Arguments
iv)Required Arguments

Default arguments:
We can provide a default value while creating a function. 
This way the function assumes a default value even if a value is not provided in the function call for that argument.
Example:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
#calling function
name("Amy")
Output:
Hello, Amy Jhon Whatson

Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
Hence, the the order in which the arguments are passed does not matter.
Example:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
#calling function
name(mname = "Peter", lname = "Wesker", fname = "Jade")
Output:
Hello, Jade Peter Wesker

Required arguments:
In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order 
and the number of arguments passed should match with actual function definition.
Example 1: when number of arguments passed does not match to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
#calling function
name("Peter", "Quill")
Output:
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'

Example 2: when number of arguments passed matches to the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
Output:
Hello, Peter Ego Quill

Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. 
This can be done using variable-length arguments.
There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of tuple.
Example:
def name(*name):
    print("Hello,", name[0], name[1], name[2])
#calling function
name("James", "Buchanan", "Barnes")
Output:
Hello, James Buchanan Barnes

Keyword Arbitrary Arguments:
While creating a function, pass a ** before the parameter name while defining the function. 
The function accesses the arguments by processing them in the form of dictionary.
Example:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")
Output:
Hello, James Buchanan Barnes
___________________________________________________________________________________________________________________________________________________________
Return Statement
The return statement is used to return the value of the expression back to the calling function.
Example:
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
    
ans = name("James", "Buchanan", "Barnes")
print(ans)
Output:
Hello, James Buchanan Barnes
'''