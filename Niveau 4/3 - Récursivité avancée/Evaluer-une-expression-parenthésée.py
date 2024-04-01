from sys import stdin
from string import digits
from operator import add, sub, mul, floordiv, mod

last_char = stdin.read(1)

def characters():
    global last_char
    while last_char != "\n":
        yield last_char
        last_char = stdin.read(1)
    yield "\n"
   
def read_integer():
    global last_char
    sign = "+"
    if last_char == "-":
        sign = next(characters())
    elif not last_char in digits:
        return None
    digits_list = []
    while last_char in digits:
        digits_list.append(next(characters()))
    number = int("".join(digits_list))
    return number if sign == "+" else -number

operators = {"+": add, "-": sub, "*": mul, "/": floordiv, "%": mod}

def read_expression():
    number = read_integer()
    if number is not None:
        return number
    next(characters())  # '('
    number1 = read_expression()
    operation = next(characters())
    number2 = read_expression()
    next(characters())  # ')'
    return operators[operation](number1, number2)

print(read_expression())
