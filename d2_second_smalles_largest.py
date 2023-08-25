def find_second_largest_smallest(arr):

    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
        
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_smallest, second_largest

arr = [12, 5, 23, 8, 19, 7]
second_smallest, second_largest = find_second_largest_smallest(arr)

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
