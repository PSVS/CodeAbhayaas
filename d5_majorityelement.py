'''#sorting
def majority(arr):
    n= len(arr)
    arr.sort()
    return arr[n/2]

'''
#By moore algorithm
def majorityelement(arr):
    n = len(arr)
    count =0
    majority = 0
    for i in range(n):
        if count == 0:
            majority = arr[i]
        if majority == arr[i]:
            count += 1
        else:
            count -=1
    return majority

arr = [1,2,3,1,2,1,1,1]
print(majorityelement(arr))
