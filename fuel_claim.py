# input variables
miles_traveled = float(input("Input your miles traveled: "))
engine_size = float(input("Input your car engine size in litres: "))
upper_limit = 1.3
#if statement engine size and fuel calculation
if ( engine_size <= upper_limit ):
    fuel_allowance = 25
    print("Your fuel allowance is 25p per litre")

else:
    fuel_allowance = 35
    print("your fuel allowance is 35p per litre")

#calculation
fuel_claim = miles_traveled * fuel_allowance

print(f"{miles_traveled:.2f} for {engine_size} results £{fuel_claim:.2f}")
