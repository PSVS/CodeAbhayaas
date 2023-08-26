#Finding missing number in array
def missing(arr):
    #Approch 1
    '''xor = 0
    for i in range(1,len(arr)+2):
        xor = xor ^ i
    for i in arr:
        xor = xor ^ i
    return xor'''
    #Approch 2
    n = len(arr)+1
    total = (n*(n+1))//2
    for i in arr:
        total -= i
    return total

arr = [1,2,5,4]
print(missing(arr))
