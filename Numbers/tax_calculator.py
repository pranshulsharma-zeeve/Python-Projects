
def calculate_tax():
    amnt = float(input("Enter the amount: "))
    tax_rate = float(input("Enter the tax rate in your country: "))
    tax_amnt = amnt * (tax_rate/100)
    white_money = amnt - tax_amnt
    print(f"Tax amount is: {tax_amnt:.2f}")
    print(f"White amount is: {white_money:.2f}")

calculate_tax()