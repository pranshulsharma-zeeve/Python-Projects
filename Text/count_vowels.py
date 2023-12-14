# def count_vowels(s):
#     vow = 'aeiouAEIOU'
#     cnt = 0
#     for i in s:
#         if i in vow:
#             cnt += 1
# 
#     print(cnt)
# 
# 
# s = str(input("Enter the string: "))
# count_vowels(s)

vowels = ['a', 'e', 'i', 'o', 'u']
counter = [0, 0, 0, 0, 0]


def count_vowels(string):
    for i in range(0, 5):
        counter[i] = string.count(vowels[i])
        # print(counter[i])


count_vowels(input('String: '))

for i in range(0, 5):
    print(vowels[i] + ": " + str(counter[i]))
