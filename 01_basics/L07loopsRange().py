'''
Introduction to Loops:
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops.


* for Loop:
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries!

Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")
Output:
A, b, h, i, s, h, e, k,

Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
Output:
Red
Green
Blue
Yellow

Similarly, we can use loops for lists, sets and dictionaries.
___________________________________________________________________________________________________________________________________________________
* range(x,y,z): x-start (by-default=0) | y-end (n-1 wala hisaab yha bhi lgega) | z-step (kitne ka jump chahiye)(by-default=1)
What if we do not want to iterate over a sequence? 
What if we want to use for loop for a range?

Here, we can use the range() function.

Example:
for k in range(5): # i.e from 0 to 5-1=4
    print(k)
Output:
0
1
2
3
4

Example:
for k in range(4,9):
    print(k)
Output:
4
5
6
7
8

Example:
for k in range(1,10,2):
    print(k)
Output:
1
3
5
7
9
______________________________________________________________________________________________________________________________________________
* while Loop:
As the name suggests, while loops execute statements while the condition is True. 
As soon as the condition becomes False, the interpreter comes out of the while loop.

Example:
count = 5
while (count > 0):
  print(count)
  count = count - 1
Output:
5
4
3
2
1
__________________________________________________________________________________________________________________________________________________
* do-while loop (not present in python, isme atleast ek baar to code execute hota hi h)
syntax:
do{

}while(condition)
'''
