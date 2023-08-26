#Left Rotate by k positions
def reverse(arr, start, end):
    while(start<end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def LeftRotate(arr, k):
    if k>len(arr):
        k = k%len(arr)

    arr = reverse(arr,0,k-1)
    arr = reverse(arr,k, len(arr)-1)
    arr = reverse(arr, 0, len(arr)-1)
    return arr


arr = [0,1,2,3,4,5]
k =13
print(LeftRotate(arr,k))
