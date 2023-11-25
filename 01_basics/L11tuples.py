'''
* Tuples are ordered collection of data items. 
They store multiple items in a single variable. 
Tuple items are separated by commas and enclosed within round brackets (). 
Tuples are immutable/unchangeable meaning we can not alter them after creation.

Example 1:
tuple1 = (1,2,2,3,5,4,6)
print(tuple1)
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
Output:
(1, 2, 2, 3, 5, 4, 6)
('Abhijeet', 18, 'FYBScIT', 9.8)
_________________________________________________________________________________________________________________________
* tuple indexing & accessing 
* to check xyz present in tuple or not
* range/slicing of tuple
EXACTLY SAME AS LIST but 1)can't change values as tpl[0]='white' (not-possible)
                         2)after applying tuple methods/slicing, returns new tuple as tuples are immutable!
________________________________________________________________________________________________________________________________
* Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, 
then first you must convert the tuple to a list. 
Then perform operation on that list and convert that list back to tuple.

Example:
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
Output:
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

However, we can directly concatenate two tuples without converting them to list.
Example:
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
Output:
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
_______________________________________________________________________________________________________________________
* Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods.
They are explained below:
1)len(tpl)
2)count() method of Tuple returns the number of times the given element appears in the tuple.
Example
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
Output
3

3)Index() method returns the first occurrence of the given element from the tuple.
Note: This method raises a ValueError if the element is not found in the tuple.
Example
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
Output
3
'''