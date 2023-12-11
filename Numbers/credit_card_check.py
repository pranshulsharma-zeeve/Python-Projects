
def checksum(num):
    def digit_of(num):
        return [int(d) for d in str(num)]
    digit = digit_of(num)
    odd = digit[-1::-2]
    even = digit[-2::-2]
    ch_sum = 0
    ch_sum += sum(odd)
    for d in even:
        ch_sum += sum(digit_of(d*2))
    return ch_sum % 10
card_num = str(input("Enter 16 digit Card Number: "))
print("Valid") if checksum(card_num)==0 else print("Invalid")