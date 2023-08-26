def UnionOfArray(arr1, arr2):
    '''res = arr1+ arr2
    res = set(res)
    res = list(res)'''
    union = []
    
    for element in arr1:
        if element not in union:
            union.append(element)
    
    for element in arr2:
        if element not in union:
            union.append(element)
    
    return union

arr1 = [1,2,3,3,4,5]
arr2 = [2,3,4,6,7,8]
print(UnionOfArray(arr1,arr2))
