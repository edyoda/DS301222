user_input=int(input("enter a number to check weather positive or negative: "))
if user_input<0:
    print("number is negative",user_input)
elif user_input == 0:
    print("number is neutral",user_input)
else:
    print("number is positive",user_input)    

num=int(input("enter num"))
if num<0:
    print(num ,"is +ve")
else:
    print(num,"is -ve")
