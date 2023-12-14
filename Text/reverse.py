# def rev(s):
#     n_s = s[::-1]
#     print(n_s)
#

def reverse_string(s):
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


s = str(input("Enter the string: "))
# rev(s)
print(reverse_string(s))
