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
