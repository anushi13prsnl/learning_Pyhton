"""
* Variable is like a container that holds data(in python need not specify var, int to declare):
a = 1
b = True
c = "Harry"
d = None

* Data type specifies the type of value a variable holds.
  2 types - built-in & user-made.
In python, we can print the type of any operator using type function - type() :                               """
a = 1
print(type(a))  #int
b = "1"
print(type(b))  #string
c= 1.0
print(type(c))  #float

'''
By default, python provides the following built-in data types:
[BY DEFAULT IN PYTHON EVERYTHING IS AN OBJECT - will discuss this later...]

1. Numeric data: int, float, complex
int: 3, -8, 0
float: 7.349, -9.0, 0.0000001
complex: 6 + 2i

2. Text data: str
str: "Hello World!!!", "Python Programming"

3. Boolean data:
Boolean data consists of values True or False.

4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. 
Lists are mutable and can be modified after creation.
Example:
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

Output:
[8, 2.3, [-4, 5], ['apple', 'banana']]

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses.
Tuples are immutable and can not be modified after creation.
Example:
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

Output:
(('parrot', 'sparrow'), ('Lion', 'Tiger'))

5. Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

Output:
{'name': 'Sakshi', 'age': 20, 'canVote': True}                                                  


* Operators
Python has different types of operators for different operations. 
To create a calculator we require arithmetic operators.

Arithmetic operators:
Operator	Operator Name	Example
+	       Addition	         15+7
-	       Subtraction     	 15-7
*	       Multiplication	 5*7
**         Exponential	     5**3
/	       Division	         5/3
%	       Modulus	         15%7
//	       Floor Division	 15//7 (to only int value in answer after division without rounding-off)

Exercise:                                                                                             '''
n = 20
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
