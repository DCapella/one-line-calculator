import re

def addition(solution, number):
    return solution + number

def subtraction(solution, number):
    return solution - number

def multiplication(solution, number):
    return solution * number

def division(solution, number):
    return solution / number

def power(solution, number):
    return solution ** number

def expression():
    expression = input(">> ")
    expression = re.sub('\s+', '', expression)
    return expression

def get_selection(character, symbol, solution):
    symbols = {
        '+' : addition,
        '-' : subtraction,
        '/' : division,
        '*' : multiplication,
        'x' : multiplication,
        'X' : multiplication,
        '^' : power,
        '**': power
    }
    # symbols['*', 'x', 'X'] = multiplication
    symbols['^', '**'] = power
    answer = symbols.get(symbol, lambda: "nothing")
    return answer(solution, character)

def calculate(expression):
    count = 0
    solution = 0
    symbol = '+'

    for character in expression:
        try:
            character = int(character)
            solution = get_selection(character, symbol, solution)
            count = 0
        except Exception as e:
            if count > 0:
                symbol = '**'
            else:
                symbol = character
            count += 1

    return solution
