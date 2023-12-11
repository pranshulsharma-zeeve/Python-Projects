def converter(unit1, val1):
    if unit1 == 'celsius':
        return (val1 * 9 / 5) + 32
    else:
        return (val1 - 32) * 5 / 9


unit1 = input("Enter unit that you want to convert like celsius/fahrenheit: ")
val1 = float(input("Enter the value that you wanted to convert: "))
result = converter(unit1, val1)
if unit1 == 'celsius':
    print(f"The value converted from {unit1} to fahrenheit is: {result:.2f}")
else:
    print(f"The value is converted from {unit1} to celsius: {result:.2f} ")
