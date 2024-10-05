
import argparse
import re
import math
import sys
import os
import inspect
import textwrap
import readline
import rlcompleter
from sympy import symbols, Eq, solve
from utils.number_theory import gcd, lcm, modinv, eea
from utils.bitwise import ror, rol, xor
from utils.stochastic import nCr, nPr
from utils.prime import isprime, nextprime
from utils.convert_base import bin2dec, dec2bin, hex2dec, dec2hex, oct2dec, dec2oct, bin2hex, hex2bin, bin2oct, oct2bin, hex2oct, oct2hex

HISTORY_FILE = os.path.expanduser("~/.acc_history")

# Load history if it exists
if os.path.exists(HISTORY_FILE):
    readline.read_history_file(HISTORY_FILE)

# Dictionary of allowed functions for safe evaluation
SAFE_FUNCTIONS = {
    'gcd': gcd,
    'lcm': lcm,
    'modinv': modinv,
    'eea': eea,
    'nCr': nCr,
    'nPr': nPr,
    'isprime': isprime,
    'nextprime': nextprime,
    'ror': ror,
    'rol': rol,
    'xor': xor,
    'bin2dec': bin2dec,
    'dec2bin': dec2bin,
    'hex2dec': hex2dec,
    'dec2hex': dec2hex,
    'oct2dec': oct2dec,
    'dec2oct': dec2oct,
    'bin2hex': bin2hex,
    'hex2bin': hex2bin,
    'bin2oct': bin2oct,
    'oct2bin': oct2bin,
    'hex2oct': hex2oct,
    'oct2hex': oct2hex,
    # math builtin functions
    'sqrt': math.sqrt,
    'pow': math.pow,
    'log': math.log,
    'log10': math.log10,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
  }

SAFE_CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
}

VALID_VARIABLE_NAME = re.compile(r"^[a-zA-Z_]\w*$")

def define_variable(input, variables, safe_dict):
    """Define a new variable from user input"""
    try:
        var_name, var_value = input.split("=")
        var_name = var_name.strip()
        var_value = var_value.strip()

        if not VALID_VARIABLE_NAME.match(var_name):
            print(f"Invalid variable name {var_name}")
            return
       
        var_value_evaluated = safe_eval(var_value, {**safe_dict, **variables})
        variables[var_name] = var_value_evaluated
    except Exception as e:
        print(f"Error in variable assignment: {e}")

def safe_eval(expression, safe_dict):
    """Evaluate an arithmetic expression with restricted functions."""
    try:
        return eval(expression, {"__builtins__": None}, safe_dict)
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero is undefined.")
    except ValueError as e:
        raise ValueError(f"Math error: {e}")
    except Exception as e:
        #raise ValueError(f"evaluating expression: {e}")
        raise ValueError(e)

def solve_equation(user_input, variables):
    """Solve an equation provided by the user"""
    try:
        lhs, rhs = user_input.split('=')
        lhs = lhs.strip()
        rhs = rhs.strip()

        # Convert variables into SymPy symbols
        sympy_vars = {var: symbols(var) for var in variables.keys()}
        
        # Add user variables to the environment
        sympy_vars.update({var: symbols(var) for var in lhs.split() + rhs.split() if var.isalpha()})

        # Parse and solve the equation
        equation = Eq(eval(lhs, {"__builtins__": None}, {**SAFE_FUNCTIONS, **sympy_vars, **variables}),
                      eval(rhs, {"__builtins__": None}, {**SAFE_FUNCTIONS, **sympy_vars, **variables}))
        solution = solve(equation)
        print(f"{solution}")
    except Exception as e:
        print(f"Error solving equation: {e}")

def is_assignment(user_input):
    """Check if the input is a variable assignment."""
    if '=' in user_input:
        var_name, _ = user_input.split("=")
        var_name = var_name.strip()
        # Check if the left-hand side is a valid variable name
        return VALID_VARIABLE_NAME.match(var_name)
    return False

def print_help():
    """Prints help information dynamically, grouped by the module from which each function is imported."""
    print("This is an Advanced Command Line Calculator\n")
    
    all_items = []

    # Organize functions by their module
    functions_by_module = {}
    for func_name, func in SAFE_FUNCTIONS.items():
        if callable(func): 
            module = func.__module__
            if module not in functions_by_module:
                functions_by_module[module] = []
            # Get the function signature (arguments)
            try:
                signature = str(inspect.signature(func))
                # Remove positional-only notation '/'
                signature = re.sub(r",? /\)", ")", signature)
            except ValueError:
                signature = "()"
            # Append the function, signature, and description
            functions_by_module[module].append((func_name, signature, func.__doc__ or "No description available."))
            all_items.append((func_name, signature))  # Add for global max width calculation

    # Add constants to all_items for width calculation
    for const_name, const_value in SAFE_CONSTANTS.items():
        all_items.append((const_name, ""))

    max_width = max(len(f"{name}{signature}") for name, signature in all_items) + 10

    # Print functions organized by their module with formatted output
    for module, funcs in functions_by_module.items():
        print(f"{module.capitalize()}:")

        for func_name, signature, doc in funcs:
            # Format the function name, signature, and description
            func_info = f"    {func_name}{signature}"
            
            # Align the description by padding the function info to max_width
            padding = ' ' * (max_width - len(func_info))
            
            # Wrap the description to a max width of 80 characters, with subsequent lines indented
            wrapped_description = textwrap.fill(doc, width=80, subsequent_indent=' ' * max_width)
            
            # Combine the function info and the wrapped description
            print(f"{func_info}{padding}{wrapped_description}")
        
        print()

    # Print constants separately, aligned with the functions
    print("Available constants:")
    for const_name, const_value in SAFE_CONSTANTS.items():
        const_info = f"    {const_name}"
        padding = ' ' * (max_width - len(const_info))
        print(f"{const_info}{padding}{const_value}")
    
    print()
    print("Type 'exit' to quit the calculator.")

def completer(text, state):
    """Function for auto-completion"""
    options = [key for key in SAFE_FUNCTIONS.keys() if key.startswith(text)] + \
              [key for key in SAFE_CONSTANTS.keys() if key.startswith(text)]

    #               [key for key in variables.keys() if key.startswith(text)] + \

    
    if state < len(options):
        return options[state]
    else:
        return None

    print(SAFE_CONSTANTS)
    print(options)

def main():
    print("Welcome to the Advanced Command Line Calculator!")
    print("Type your expression or type 'exit' to quit.")
    
    safe_dict = {**SAFE_FUNCTIONS, **SAFE_CONSTANTS}  # Load safe functions
    variables = dict()

    # Enable tab completion using the readline and rlcompleter modules
    readline.set_completer(completer)
    readline.parse_and_bind("set enable-keypad on")  # Enable the keypad mode
    #readline.parse_and_bind("tab: complete")
    readline.parse_and_bind(r'"\C-m": complete')

    while True:
        try:
            user_input = input(">>> ")

            # Check if user wants to exit
            if user_input.lower() in ['exit', 'quit']:
                print("Bye!")
                break
            
            # Print Help
            if user_input.lower() == "help":
                print_help()
                continue

            # Add variable support
            if "=" in user_input:
                if not is_assignment(user_input):
                    solve_equation(user_input, variables)
                else:
                    define_variable(user_input, variables, safe_dict)
                continue

            # Try to evaluate the input expression
            try:
                result = safe_eval(user_input, {**safe_dict, **variables})
                print(result)
            except Exception as e:
                print(f"Error: {e}")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

    # At the end of your program, save the history
    try:
        readline.write_history_file(HISTORY_FILE)
    except IOError:
        print("Error saving history file")


if __name__ == "__main__":
    main()
