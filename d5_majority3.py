def majorityn3(arr):
    count1, count2 = 0, 0
    first,  second = None, None

    for i in range(len(arr)):
        if first == arr[i]:
            count1 += 1
        elif second == arr[i]:
            count2 += 1
        elif count1 == 0:
            count1 =1
            first = arr[i]
        elif count2 == 0:
            count2 =1
            second = arr[i]
        else:
            count1 -=1
            count2 -= 1

    count1, count2 = 0,0
    
    for i in range(len(arr)):
        if first == arr[i]:
            count1 += 1
        elif second == arr[i]:
            count2 += 1

    if count1> len(arr)/3:
        return first
    if count2> len(arr)/3:
        return second


arr = [1, 2, 3, 1, 1 ]
print(majorityn3(arr))
            
