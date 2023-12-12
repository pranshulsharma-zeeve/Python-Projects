
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            print(p)

n = int(input("Enter the number: "))
print("Following are the prime numbers: ")
sieve_of_eratosthenes(n)