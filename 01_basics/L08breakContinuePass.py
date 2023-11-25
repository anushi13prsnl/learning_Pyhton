# one thing to notice - jo main-code h usse phele we put break/continue statement bcz we check immediately for the value of i(iterarion no.)

'''
The break statement enables a program to skip over a part of the code. 
A break statement terminates the very loop it lies within.
break says loop hi chod doo please!
'''
for i in range(1,15,1):
    if(i==5):
        break
    print(i) #main-code
print("Thank you")
# output-
# 1
# 2
# 3
# 4
# Thank you




'''
Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
continue says jis line m mai aa gya usse niche kuch execute nhi hoga and agli iterartion pr chle jao!
'''
for i in range(1,15,1):
    if(i==5):
        continue
    print(i) #main-code
print("Thank you")
# output-
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# Thank you

'''
Pass statement is used as a placeholder for future code.
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
Examples:


def myfunction():
  pass


class Person:
  pass
  

a = 33
b = 200
if b > a:
  pass
'''