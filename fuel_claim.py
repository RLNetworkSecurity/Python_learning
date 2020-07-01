#variables_fixed
UPPER_LIMIT = 1.3
UPPER_RATE = 35
LOWER_RATE = 25
# input variables
miles_traveled = float(input("Input your miles traveled: "))
engine_size = float(input("Input your car engine size in litres: "))

#if statement engine size and fuel calculation
if ( engine_size <= UPPER_LIMIT ):
    fuel_allowance = LOWER_RATE
else:
    fuel_allowance = UPPER_RATE

#calculation
fuel_claim = miles_traveled * fuel_allowance/100

#output
print(f"{miles_traveled:.2f} for {engine_size} results £{fuel_claim:.2f}")
