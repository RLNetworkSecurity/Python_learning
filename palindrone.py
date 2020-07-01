# input variables
input_word = input("Input your potential palindrome: ")
nospace_word = input_word.replace(" ","")
reverse_word = nospace_word[::-1]

# if statement engine size and fuel calculation
if input_word == reverse_word:
    print(f" your word{input_word} is a palindrome as shown: {reverse_word}")
else:
    print(f" your word{input_word} is not a palindrome as shown: {reverse_word}")
