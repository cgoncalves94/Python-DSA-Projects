import random

# Bubble Sort algorithm
# Takes an array and a comparison function as arguments
# Sorts the array based on the comparison function
def bubble_sort(arr, comparison_function):
    swaps = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                is_sorted = False
                # Swap elements
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print("Bubble sort: There were {0} swaps".format(swaps))
    return arr

# Quick Sort algorithm
# Takes a list, start and end indices, and a comparison function as arguments
# Sorts the list based on the comparison function
def quicksort(list, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, list[i]):
            # Swap elements
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer - 1, comparison_function)
    quicksort(list, less_than_pointer + 1, end, comparison_function)
