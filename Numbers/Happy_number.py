
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num==1

count = 0
number = 1
record = []
while(count < 8):
    if is_happy(number):
        record.append(number)
        count += 1
    number += 1

print(f"8 Happy number: {record}")
