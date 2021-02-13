from art import logo

def calculate(number1, number2, expression):
    mathematical_expression = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2,
        '/': number1 / number2
    }

    print(mathematical_expression.get(expression, "Invalid"))

calculate(1,2,'/')