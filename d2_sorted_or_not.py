def is_sorted(arr):
    n = len(arr)
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True


sorted_arr = [1, 3, 5, 7, 9]
unsorted_arr = [8, 2, 6, 4, 10]

print("Is sorted_arr sorted?", is_sorted(sorted_arr))
print("Is unsorted_arr sorted?", is_sorted(unsorted_arr))
