#while loop example
again = "Y"

#start loop
while again in ["y", "Y", "yes"]:
    
    table_number = int(input("Input yoru times table: ")) 
    number_rows = int(input("Input row_number: "))

    #display heading
    print(f"{table_number} times table")
    print("-"*60)

    #for loop examples

    for row in range(number_rows+1):
        answer = table_number * row
        print(f"{row:3} * {table_number} = {answer:4}")

    #do they want to run again?
    again = input("Again (y/n):")
