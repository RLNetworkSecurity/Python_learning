# input variables
import re
input_word = input("Input your potential palindrome: ")
clean_word = re.sub('[^A-Za-z]+', '', input_word)
reverse_word = clean_word[::-1]

# if statement engine size and fuel calculation
if new_word == reverse_word:
    print(f" your word{input_word} is a palindrome as shown: {clean_word}")
else:
    print(f" your word {input_word} is not a palindrome as shown: {clean_word}")
