def is_palin(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# def is_palin(s):
#     return s == s[::-1]


s = str(input("Enter the string: "))
if is_palin(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
