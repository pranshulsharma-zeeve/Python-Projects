
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primefun():
    num = 2
    while True:
        select = input(f"Do you want the next prime number yes/no: ")
        if select.lower() == 'yes':
            yield num
            num += 1
            while not isprime(num):
                num += 1
        elif select.lower() == 'no':
            print("Exiting..")
            break
        else:
            print("please enter yes or no")


prime = primefun()
for p in prime:
    print(p)
    pass
