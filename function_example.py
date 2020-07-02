#CONSTANTS
DEGC = "\u2103"
DEGF = "\u2109"

# define functions
def c_to_f(num):
    return (num * 9/5) + 32

#reverse function
def f_to_c(num):
    return (num - 32) * 5/9

# code
function_input = float(input(f"input your temperature in {DEGC}"))
function_output_f = c_to_f(function_input)
print(f"your output is {function_output_f}{DEGF}")

#code
function_output_c = f_to_c(function_output_f)
print(f"your output is {function_output_c}{DEGC}")
