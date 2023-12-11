
def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr ) - i -1):
            if arr[j] > arr[ j +1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break

arr = []
n = int(input("Enter the size of array you want: "))
for _ in range(n):
    ele = input()
    arr.append(ele)

bubbleSort(arr)
print(f"Sorted array is {arr}")
