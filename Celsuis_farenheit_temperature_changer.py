DEGC = "\u2103"
DEGF = "\u2109"
degrees_celsius = float(input("input your temperature in {DEGC}"))
degrees_fahrenheit = (degrees_celsius * 9/5) + 32
print(f"{degrees_celsius:.1f}{DEGC} is {degrees_fahrenheit:.1f}{DEGF}")
