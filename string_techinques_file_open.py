#Change print seperator i.e to @

print("Hello","Frank",sep="@")

#Print in CSV

print("Hello","Frank",sep=",")

#Default print end
print("Hello", end="\n")

#no end to print
print("Hello", end="")

#Send to a file - quick and dirty way, useful for logging
#w will write to the file, a will append
myfile = open("mydata.txt","w")
print("Hello", file=myfile,flush=True)
#user backslash to escape the meaning of it
myfile = open("c:\\mydata.txt","w")

#print a raw string
print(r"c:\newdata.txt")

#open explicit file for append
open(r"c:\newdata.txt","a")

#find and replace example
link = "https://cyprotect.co.uk"
link.replace("https","ftp")

# multiple a string
NQQ * 4
