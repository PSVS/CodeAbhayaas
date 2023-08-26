#Reverse an array
def reverseArray(arr):
    start = 0
    end = len(arr)-1
    while(start<=end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [90,80,70,60,50,40,30,30,20,10]
print(reverseArray(arr))
