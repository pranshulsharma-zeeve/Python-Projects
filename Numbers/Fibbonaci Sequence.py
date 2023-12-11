
def solve(n):
    li=[]
    li.append(0)
    li.append(1)
    c=2
    for i in range(0,n):
        if c < n:
            li.append(li[i]+li[i+1])
            c+= 1
        else:
            break
    return li

try:
    N = int(input("Enter the Number: "))
    if N > 0:
        li = solve(N)
        print(f"Fib. Sequence upto N : {li}")

    else:
        print("Please enter positive number")

except ValueError:
    print("please enter valid number: ")