'''* Docstrings in python '''
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

# Example_01:
# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
#calling function
# square(5)
# Here, '''Takes in a number n, returns the square of n''' is a docstring which will not appear in output
# Output:
# 25

# Example_02:
# def add(num1, num2):
#     """
#     Add up two integer numbers.
#     This function simply wraps the ``+`` operator, and does not
#     do anything interesting, except for illustrating what
#     the docstring of a very simple function looks like.
#     """
#     return num1 + num2
'''
Python Comments vs Docstrings
Python Comments
Comments are descriptions that help programmers better understand the intent and functionality of the program. 
They are completely ignored by the Python interpreter.

Python docstrings
As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). 
They are used to document our code.
Unlike comments, We can access these docstrings using the doc attribute, by print(square.__doc__) # __ is 2 times underscore.
Example                                                                                               '''
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
print(square.__doc__)

# Output:
# Takes in a number n, returns the square of n
'''_______________________________________________________________________________________________________________________________________________________



* PEP 8 is a document that provides guidelines and best practices on how to write Python code. 
It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
The primary focus of PEP 8 is to improve the readability and consistency of Python code.

* PEP stands for Python Enhancement Proposal, and there are several of them. 
A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

* The Zen of Python
Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms, only 19 of which have been written down.
i.e. when we give cmd on terminal -> import this 
we get a poem - The Zen of Python :)
'''
