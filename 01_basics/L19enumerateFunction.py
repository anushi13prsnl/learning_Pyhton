'''
* Enumerate function in python:
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) 
and get the index and value, BOTH, of each element in the sequence at the same time. 

* Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

The output of this code will be:
0 apple
1 banana
2 mango
___________________________________________________________________________________________________________________________________________
* can modify starting index from 1, instead of 0
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

This will output:
1 apple
2 banana
3 mango
'''