

def solve(n):
    dec = 0
    power = len(n) - 1
    for digit in n:
        if digit == '1':
            dec += 2 ** power
        power -= 1
    return dec


try:
    N = (input("Enter the binary number: "))

    decimal = solve(N)
    print(f"Decimal value is: {decimal}")


except ValueError:
    print("please enter valid number: ")