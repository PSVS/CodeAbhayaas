#Finding Max and Min element in an array
def MaxMin(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in arr:
        if i<mini:
            mini = i
        if i>maxi:
            maxi = i
    return mini, maxi

arr = [0,-1,9,11,8,22,18,55]
minimum, maximum = MaxMin(arr)
print("Minimum is ", minimum)
print("Maximum is ", maximum)
    
    
