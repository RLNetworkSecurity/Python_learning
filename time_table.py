#while loop example

table_number = int(input("Input yoru times table: ")) 
number_rows = int(input("Input row_number: "))

#display heading
print(f"{table_number} times table")
print("-"*60)

#for loop examples

for row in range(number_rows+1):
    answer = table_number * row
    print(f"{row:3} * {table_number} = {answer:4}")
