from art import logo

def calculate(number1, number2, operation):
    mathematical_expression = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2,
        '/': number1 / number2
    }
    answer = mathematical_expression.get(operation, "Invalid")
    print(f"{number1} {operation} {number2} = {answer}")

print(logo)
number1 = int(input("What's the first number?: "))
number2 = int(input("What's the second number?: "))
operation = input("What operation would you want? + - * /: ")
calculate(number1, number2, operation)