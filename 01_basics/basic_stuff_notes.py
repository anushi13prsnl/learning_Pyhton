'''
It's just intro...
why python
about modules
pip cmd
comments
print() & escape sequences


___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
* why python ? --> 
dynamically programmed lang + platform independent lang.

* about modules -->
Module is like a code library which can be used to borrow code written by somebody else in our python program. 
There are two types of modules in python:
Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.
  We use the import syntax to import a module in Python. Here is an example code:
  import pandas

* pip command -->
It can be used as a package manager pip to install a python module. 
Lets install a module called pandas using the following command:
pip install pandas

* comments -->
single-line  -  #.....
multi-line   -  ''' '''  | """ """ | can use # before start of each line 

* print(5) | output - 5 bcz int so no error
  print(anushi) | output - error as string
  print("anushi") | output - anushi | CAN USE ""/'' IN PYTHON 
  print("hi" , 6 , "world") | output - hi 6 world mtlb to add parameters we write ,
  
  (sep='separator': Specify how to separate the objects, if there is more than one. Default is ' ')
  (end='end': Specify what to print at the end. Default is '\n' (next line) )

  print("hi" , 6 , "world", sep='~') | output - hi~6~world
  print("hi" , 6 , "world", end='-') | output - hi 6 world- | mtlb ends printing with - 
  print("i am anushi, i am a "good girl" and i love exploring. " ) | output - error as "" used in text interpreter will get confused kha se shuru kha p khatam
  print("i am anushi
  and i am a good girl") | output - error as not allowed

Thus to use ""/'' in string OR nxt line while printing, need escape sequence characters...

* escape sequence character -->
To insert characters that cannot be directly used in a string, we use an escape sequence character.
An escape sequence character is a backslash \ followed by the character you want to insert.
eg. \n (for nxt line)
    \' (to add ' in string)
    \" (to add " in string)

'''