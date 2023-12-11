import random


def flip(n):
    head = 0
    tail = 0
    outcomes = []
    for i in range(n):
        outcome = random.choice(['Head', 'Tail'])
        outcomes.append(outcome)
        if outcome == 'Head':
            head += 1
        else:
            tail += 1

    return outcomes, head, tail


n = int(input("How many times do you flip the coin? : "))
result, heads, tails = flip(n)

print(f"The random outcome when you flip the coin: {result}")
print(f"Head comes {heads} times")
print(f"Tail comes {tails} times")
