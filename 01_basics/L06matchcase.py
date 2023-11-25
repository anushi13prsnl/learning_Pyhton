'''
Syntax:[ jese java m har case k baad break; lgana was compulsory, idhr nhi h:) ]
       [isme bhi yhi h ki, agr ek statement gets satisfied toh agli pdhi bhi nhi jayegi that too without using break; statement as in java(covered in above line) ]
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n

Example_01:
x = int(input())
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")

    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")

    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")

    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

Output:
x % 2 == 0 and case is 4

Example_02:                                                                                         '''

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80: #yhaa !=80(will run only for x=90) and defalut statement toh kbhi run hi nhi hogi bcz as soon as !=90 gets satisfied, it breaks!
        print(x, "is not 80")
    case _:
        print(x)