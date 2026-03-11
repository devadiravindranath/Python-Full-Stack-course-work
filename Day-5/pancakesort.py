# Pancake Sort

def flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1


def pc_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        max_index = arr.index(max(arr[:curr_size]))

        # move max element to front if it's not already there
        if max_index != 0:
            flip(arr, max_index)

        # move max element to its correct position
        flip(arr, curr_size - 1)


arr = list(map(int, input("Enter elements: ").split()))
pc_sort(arr)
print("Sorted array:", arr)
