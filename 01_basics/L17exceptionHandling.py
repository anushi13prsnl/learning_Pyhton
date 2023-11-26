'''
* Python try...except
try…except blocks are used in python to handle errors and exceptions. 
The code in try block runs when there is no error. 
If the try block catches the error, then the except block is executed.
                                                                                                      '''
#Example-1
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}") #printing table of a
# except Exception as e : #can write only except:
#   #print("Invalid  Input!") #if int ki jgh user inputs name such as harry, abh harry ka table toh bn nhi skta
#   print(e)                  #prints error

# print("Some imp lines of code")
# print("End of program")


#Example-2
# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num]) #if num=5 input aya by user, a[5] not exists, raises error named IndexError
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")

'''
éxcept k bhi types hote hai, like Indexerror/ValueError/NameError... can have multiple except in our code.

* Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.       '''

# Example_01:                                                                                                 
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# Example_02:  
# x=5
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# finally will run in both the cases [above]!

'''
but the question is finally ki zaroort kya h indentation shi krke bhi toh finally wala block bina keyword k chlta skte h
yes, but jbh function m hota h return statement whaa pnga pd jata hai!                                                             '''

# Example_01:   
# try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except:
#     print("Some error occurred")

# #   finally:
# #   print("I am always executed")
# print("I am always executed")

# Example_02:  (jbh function m return execute hota udhr problem aa jati h so need finally bcz yh toh execute hogaa hi no matter return is there or not)
# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

# #   finally:
# #     print("I am always executed")
#   print("I am always executed")


# x = func1()
# print(x) 

