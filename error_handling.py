#Error handling python

#get iser om[its
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))

#division
try:
    result = num1 / num2
    
except ZeroDivisionError as err:
    print(err)
else:
    #output result
    print(f"{num1} / {num2} is {result}")
