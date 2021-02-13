from art import logo

should_continue = True
def calculate(number1, number2, operation):
    mathematical_expression = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2,
        '/': number1 / number2
    }
    answer = mathematical_expression.get(operation, "Invalid")
    return answer

print(logo)
number1 = int(input("What's the first number?: "))

while should_continue:
    number2 = int(input("What's the next number?: "))
    operation = input("What operation would you want? + - * /: ")
    answer = calculate(number1, number2, operation)
    print(f"{number1} {operation} {number2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
        number1 = answer
    else:
        should_continue = False