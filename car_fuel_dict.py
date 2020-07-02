#variables_fixed
UPPER_LIMIT = 1.3
UPPER_RATE = 0.35
LOWER_RATE = 0.25
# input variables
miles_traveled = float(input("Input your miles traveled: "))
engine_size = input(f"Is your engine size above {UPPER_LIMIT}, answer yes or no: ")

#lookup Table
engine_size_dictionary = {"yes":UPPER_RATE, "no":LOWER_RATE,}
fuel_allowance = engine_size_dictionary[engine_size.lower()]

#calculation
fuel_claim = miles_traveled * fuel_allowance

#output
print(f"{miles_traveled:.2f} results £{fuel_claim:.2f}")
