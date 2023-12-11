def calculate(oper, num1, num2):
    if oper == 'add':
        return num1 + num2
    elif oper == 'subtract':
        return num1 - num2
    elif oper == 'multiply':
        return num1 * num2
    else:
        return num1 / num2 if num2 != 0 else "Error: Division by zero"


operation = input("Enter the operation that you want to perform like add/subtract/multiply/divide: ")
num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the second number: "))
result = calculate(operation, num1, num2)
print(f"The answer is: {result}")
