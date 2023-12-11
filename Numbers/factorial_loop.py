
def calc_factorial():
    n = int(input("Enter the Number: "))
    fact = 1
    for i in range(1,n+1):
        fact *= i

    print(f"Factorial of {n} is {fact}")

calc_factorial()