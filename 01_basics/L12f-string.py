'''
String formatting in python:

* String formatting can be done in python using the format method.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#OUT_DATED_WAY

* f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. 
It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). 
The primary focus of this mechanism is to make the interpolation easier.

-> When we prefix the string with the letter 'f', the string becomes the f-string itself.
The f-string can be formatted in much same as the str.format() method.

Example:  
name = 'Tushar'  
age = 23  
print(f"  Hello, My name is {name} and I'm {age} years old.  ")
Output:
  Hello, My name is Tushar and I'm 23 years old.

Example
print(f"{2 * 30})" #We can use it in a single statement as well.
Output:
60

-> if wanna print {name} & {age} as such in f-string, use {{...}}
Example:  
name = 'Tushar'  
age = 23  
print(f"  Hello, My name is {{name}} and I'm {{age}} years old.  ")
Output:
  Hello, My name is {name} and I'm {age} years old.
'''