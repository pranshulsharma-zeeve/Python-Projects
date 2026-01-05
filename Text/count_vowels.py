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
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowel_counter = [0, 0, 0, 0, 0]
consonant_counter = [0] * 21


def count_vowels_and_consonants(string):
    string_lower = string.lower()
    
    # Count vowels
    for i in range(0, 5):
        vowel_counter[i] = string_lower.count(vowels[i])
    
    # Count consonants
    for i in range(0, 21):
        consonant_counter[i] = string_lower.count(consonants[i])


input_string = input('String: ')
count_vowels_and_consonants(input_string)

print("\nVowel counts:")
for i in range(0, 5):
    print(vowels[i] + ": " + str(vowel_counter[i]))

print("\nConsonant counts:")
for i in range(0, 21):
    print(consonants[i] + ": " + str(consonant_counter[i]))

# Print totals
total_vowels = sum(vowel_counter)
total_consonants = sum(consonant_counter)
print("\nTotal vowels: " + str(total_vowels))
print("Total consonants: " + str(total_consonants))
