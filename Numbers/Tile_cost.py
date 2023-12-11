
def solve(w, h, cost):
    total_tiles = w*h
    final_cost = total_tiles * cost
    return final_cost


try:
    cost_per_tile = float(input("Enter the cost of each tile: "))
    w = float(input("Enter the width: "))
    h = float(input("Enter the height: "))
    if w>0 and h>0 and cost_per_tile>0:
        total_cost = solve(w, h, cost_per_tile)
        print(f"Total cost to cover floor with tile: rs{total_cost:.2f}")

    else:
        print("Enter valid positive values: ")


except ValueError:
    print("please enter valid number: ")