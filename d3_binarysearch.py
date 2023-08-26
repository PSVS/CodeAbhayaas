#Recursive approch
'''def binary_search(arr,start,end,key):
    if start<end:
        return False
    else:
        mid = int((start+end)/2)
        if arr[mid] == key:
            return mid
        elif key>arr[mid]:
            return binary_search(arr, mid+1, end, key)
        else:
            return binary_search(arr, start, mid-1, key)
'''
#Iterative approach
def binary_search(arr, start, end, key):
    while (start <= end):
        mid = int((start+end)/2)
        if arr[mid] == key:
            return mid
        elif key>arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False


arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(arr,0, len(arr)-1,10))
