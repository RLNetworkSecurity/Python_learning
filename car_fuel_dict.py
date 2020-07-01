#variables_fixed
UPPER_LIMIT = 1.3
UPPER_RATE = 35
LOWER_RATE = 25
# input variables
miles_traveled = float(input("Input your miles traveled: "))
engine_size = (input(f"Is your engine size above {UPPER_LIMIT}, answer yes or no: "))

engine_size_dictionary = {"yes":35, "no":20,}
fuel_allowance = int(engine_size_dictionary[engine_size])
#calculation
fuel_claim = miles_traveled * fuel_allowance/100

#output
print(f"{miles_traveled:.2f} for {engine_size} results £{fuel_claim:.2f}")
