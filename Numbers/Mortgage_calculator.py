
def month_pay(rate, years, amnt):
    month_rate = rate /12 /100
    months = years * 12
    monthly_payment = (amnt * month_rate) / (1 - (1 + month_rate) ** -months)
    return monthly_payment


def total_pay(monthly_amt,year):
    return monthly_amt* year* 12



try:
    principle_amount = float(input("Enter the Mortgage amount: "))
    rate = float(input("Enter the annual interest rate(in %): "))
    years = float(input("Enter the time (years): "))
    if principle_amount>0 and rate>0 and years>0:
        monthly_payment = month_pay(rate, years, principle_amount)
        total_payment = total_pay(monthly_payment, years)
        print(f"Amount per month is : rs{monthly_payment:.2f}")
        print(f"Total Payment: rs{total_payment:.2f}")

    else:
        print("Enter valid positive values: ")


except ValueError:
    print("please enter valid numbers: ")
