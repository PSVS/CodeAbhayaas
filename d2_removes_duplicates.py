def remove_duplicates(arr):
    unique_elements = set()
    result = []
    
    for num in arr:
        if num not in unique_elements:
            unique_elements.add(num)
            result.append(num)
    
    return result


arr = [5, 2, 9, 2, 3, 5, 8]
unique_arr = remove_duplicates(arr)

print("Original Array:", arr)
print("Array with Duplicates Removed:", unique_arr)
