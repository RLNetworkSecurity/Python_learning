#defines a new class we can use to create an object

class palindrome:

    def __init__ (self, mytext):
       self.__texttocheck = mytext          #property (data inside the object)
       print("Loaded:", self.__texttocheck)

    def is_palindrome(self):
        cleanstring = self.__texttocheck.replace(" ","")
        if cleanstring == cleanstring[::-1]:
            return True
        else:
            return False

#main program starts here

#creating two new OBJECTS using hte palindrome Class
new_pal = palindrome("racecars")
new_pal2 = palindrome("a nut for a jar of tuna")

#check to see if the text is indeed a palindrome
print(new_pal.is_palindrome())

#check to see if the second
print(new_pal2.is_palindrome())
