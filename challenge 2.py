num1 = int(input("insert the first number"))
num2 = int(input("insert the second number"))

kind = input("what is kind of operation")

if (kind == "+"):
    print("the sum is ", num1+num2)
elif (kind == "-"):
     print("the subb is ", num1-num2)   
elif (kind == "*"):
     print("the mull is ", num1*num2) 
else:
     print("we don't support this operation")    


