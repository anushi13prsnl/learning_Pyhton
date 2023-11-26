'''arithematic operators'''
# already done in L03

'''assignment operators'''
# Operator Assignment (=)
# Operator Addition (+=)
# Operator Subtraction (-=)
# Operator Multiplication (*=)
# Operator Division (/=)
# Operator Modulus (%=)
# Operator Exponentiation (**=)
# Operator Floor Division (//=)

'''Conditional operators'''
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

'''logical operators'''
# and	Returns True if both statements are true	
# or	Returns True if one of the statements is true	
# not	Reverse the result, returns False if the result is true


# IDENTATION is the key in conditional statements
# if condition: = if (condition):
# if not condition: [bhi hota hai]


# simple if-else ladder:
a = int(input("Enter your age: "))
if(a>18): #if(true) execute further code written under if else, shifts to else wala code
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")

# elif ladder (yha agr phla elif satisfies the condition, toh dusre ko dekha bhi nhi jayega that is it breaks as soon as condition is fulfilled, else baari baari sb check honge.)
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now") #iss statement ka upr wale ladder se koi lena dena nahi h, see INDENTATION!

# nested elif ladder
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
# _____________________________________________________________________________________________________________________________
# If ... Else in One Line:
# a = 2
# b = 330
# print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# ALL IN ALL:
# result = value_if_true if condition else value_if_false

# This syntax is equivalent to the following if-else statement:
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false