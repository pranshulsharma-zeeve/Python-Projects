from decimal import Decimal
import math


def solve(n):

    e = Decimal(0)
    for i in range(0, 100):
        e += Decimal(1) / math.factorial(i)
    return round(e, n)


try:
    N = int(input("Enter the Number of decimal places: "))
    if N <= 50:
        value = solve(N)
        print(f"e upto N decimal places: {value}")

    else:
        print("Please enter number less than 50")

except ValueError:
    print("please enter valid number: ")
