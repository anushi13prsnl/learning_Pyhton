'''
* Python Dictionaries
Dictionaries are ordered collection of data items. They store multiple items in a single variable. 
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
Output:
{'name': 'Karan', 'age': 19, 'eligible': True}

* Accessing Dictionary items:
I. Accessing single values:
Values in a dictionary can be accessed using keys. 
We can access dictionary values by mentioning keys either in square brackets or by using get method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])          #throws error when key not present
print(info.get('eligible'))  #throws NONE when key not present
Output:
Karan
True

II. Accessing all values:
We can print all the values in the dictionary using values() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
Output:
dict_values(['Karan', 19, True])

III. Accessing keys:
We can print all the keys in the dictionary using keys() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
Output:
dict_keys(['name', 'age', 'eligible'])

IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
Output:
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
'''
# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 