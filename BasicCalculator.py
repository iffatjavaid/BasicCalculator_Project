print("*"*40)
print("           Basic Calculator              ")
print("*"*40)
num1=float(input("Enter 1st No : "))
num2=float(input("Enter 2nd No: "))
operator=input("Enter an Operator: ")
if operator=="+":
    result= num1+num2
    print("Result: ",result)
elif operator=="-":
    result=num1-num2
    print("Result:  ",result)  
elif operator=="*":
    result=num1*num2
    print("Result:  ",result) 
elif operator=="/":
    if(num2==0):
        print("Division by 0 is not Valid")
    else:  
        result=num1/num2  
        print("Result:  ",result)     
elif operator=="%":
    if(num2==0):
        print("Division by 0 is not Valid")
    else:
       result=num1%num2
       print("Result:  ",result)                  
else:
    print("Invalid Operator")