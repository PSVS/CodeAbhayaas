#Find all subarrays
def subarrays(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarrays.append(arr[i:j+1])

    return subarrays

arr = [1,2,3,4,5]
print(subarrays(arr))
