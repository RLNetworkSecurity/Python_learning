#CONSTANTS
DEGC = "\u2103"
DEGF = "\u2109"

# define functions
def c_to_f(num):
    """
    this is what we call a doc string
    this function changes degrees C to degrees F
    """
    return (num * 9/5) + 32

#reverse function
def f_to_c(num):
    """
    this is what we call a doc string
    this function changes degrees F to degrees C
    """
    return (num - 32) * 5/9

# code
function_input = float(input(f"input your temperature in {DEGC}"))
function_output_f = c_to_f(function_input)
print(f"your output is {function_output_f}{DEGF}")

#code
function_output_c = f_to_c(function_output_f)
print(f"your output is {function_output_c}{DEGC}")


#function example multiple inputs, have to use the named variables in the input.
def show_chars(*, num=10, symbol="$"):
    print(symbol * num)
