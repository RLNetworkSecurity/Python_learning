import re
# input variables
input_word = input("Input your potential palindrome: ")
#prep words
clean_word = re.sub('[^A-Za-z]+', '', input_word)
reverse_word = clean_word[::-1]

# if statement to check reverse word = input word
if new_word == reverse_word:
    print(f" your word{input_word} is a palindrome as shown: {clean_word}")
else:
    print(f" your word {input_word} is not a palindrome as shown: {clean_word}")
