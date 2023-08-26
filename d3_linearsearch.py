def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False

arr = [20, 10, 50, 30, 44, 77, 33]
key = 55
if linear_search(arr, key):
    print("Element Found :)")
else:
    print("Element not found :(")
