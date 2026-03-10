import math

def jsearch(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1


arr = list(map(int, input("Enter sorted numbers with spaces: ").split()))
target = int(input("Enter element to be searched: "))

result = jsearch(arr, target)

if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print("Element not found")
