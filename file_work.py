#load the file
myfile = open("days.txt", "r")

#read the file

#everything
mydata = myfile.read()

#13 characters
mydata = myfile.read(13)

# list of the data
mydata = myfile.read.lines()

#print the file
print(mydata)


# recommended way to open files

with open('gash.txt', 'r') as infile:
    for line in infile:
        print(line, end='')

       
# create and write to a new file      
#open a file for writing
# change w to a to append to a file
with open('food_order.txt', 'w') as new_file:
    while True:
        text = input("Enter some food ('bill' = stop):")
        if text == "bill":
            break
        else:
            new_file.write(text+"\n")

print("Your order has been created")

