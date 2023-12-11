
def solve(pay, cash):
    dic = {'quarter(25rs)': 0, 'dimes(10rs)': 0, 'nickles(5rs)': 0, 'pennies(1rs)': 0 }
    left = cash - pay
    for _ in range(left):
        if left >= 25:
            dic['quarter(25rs)']+=1
            left = left - 25

        elif left >= 10:
            dic['dimes(10rs)']+=1
            left = left - 10

        elif left >= 5:
            dic['nickles(5rs)']+=1
            left = left - 5

        elif left >= 1:
            dic['pennies(1rs)']+=1
            left = left - 1
    return dic




try:
    payment = int(input("Enter the payable amount: ")) # 85
    cash = int(input("Enter the amount given by user: ")) # 100

    if payment < cash :
        change = solve(payment, cash)
        print(f"Change Amount is: {change}")

    else:
        print("You have to give more money")

except ValueError:
    print("please enter valid number: ")