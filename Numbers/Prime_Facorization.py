

def isprime(i):
    if i == 2:
        return True
    for j in range(2,i):
        if i % j == 0:
            return False
    return True


def solve(n):
    li = []
    for i in range(1, n+1):
        if isprime(i) and n%i == 0:
            li.append(i)
    return li
try:
    N = int(input("Enter the Number: "))
    if N > 0:
        fa = solve(N)
        print(f"Prime Factors of N : {fa}")

    else:
        print("Please enter positive number")

except ValueError:
    print("please enter valid number: ")