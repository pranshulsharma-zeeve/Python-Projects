from decimal import Decimal


def solve(n):
    # getcontext().prec = N + 1
    value = Decimal(22) / Decimal(7)
    return round(value, n)


try:
    N = int(input("Enter the Number of decimal places: "))
    if N <= 50:
        pi = solve(N)
        print(f"PI upto N decimal places: {pi}")

    else:
        print("Please enter number less than 50")

except ValueError:
    print("please enter valid number: ")
