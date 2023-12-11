def addition(num1, num2):
    return num1 + num2


def multiplication(num1, num2):
    return num1 * num2


def negation(num1):
    return -num1


def inversion(a):
    conjugate = a.conjugate()
    denominator = a * conjugate
    return conjugate / denominator


num1 = complex(input("Enter the first complex number: "))
num2 = complex(input("Enter the second complex number: "))
choice = int(input("Enter your choice(1,2,3,4) \n1-Addition\n2-Multiplication\n3-Negation\n4-Inversion\n: "))
if choice == 1:
    print(f"Addition of {num1} and {num2} is {addition(num1, num2)}")
elif choice == 2:
    print(f"Multiplication of {num1} and {num2} is {multiplication(num1, num2)}")
elif choice == 3:
    print(f"Negation of {num1} is {negation(num1)} ")
elif choice == 4:
    print(f"Inversion of {num1} is {inversion(num1)}")
else:
    print("Please choose number from screen only: ")