def right_rotate(arr):
    n = len(arr)
    temp = arr[n - 1]
    
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = temp

arr = [1, 2, 3, 4, 5]

print("Original Array:", arr)
right_rotate(arr)
print("Array After Right Rotation:", arr)
