
def collatz_conjucture(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3 + 1
        sequence.append(n)
    return sequence


number = int(input("Enter the number: "))
if number <= 0:
    input("Please enter the positive number: ")
else:
    seq = collatz_conjucture(number)
    print(f"The collatz sequence for {number} is: {seq}")