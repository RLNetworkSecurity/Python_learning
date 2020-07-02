#while loop example

table_number = int(input("Input your miles traveled: ")) 
number_rows = int(input("Input row_number: "))


#for loop examples

for table_number in range(number_rows):
    answer = table_number * number_rows
    print(f"{table_number} * {number_rows} = {answer}")
