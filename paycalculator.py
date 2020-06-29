hours = input("enter hours: ")
hourly_rate = input("enter hourly rate: ")
pay = float(hourly_rate) * float(hours)
tax = (pay / 100) * 20
output = pay - tax
print(f"Gross pay is £{output:.2f}")
