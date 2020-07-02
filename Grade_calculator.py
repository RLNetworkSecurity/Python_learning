# input variables
mark = int(input("enter Mark (0-100):"))

#check mark
if mark < 40:
    print("Fail")
elif mark < 65:
    print("Pass")
elif mark < 81:
    print("MERIT")
else:
    print("DISTINCTION")
