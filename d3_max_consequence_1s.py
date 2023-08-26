#count maximum of consequence 1s
def count_consequtive_1s(arr):
    count = 0
    maxi = 0
    for i in arr:
        if i == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi


arr = [0,1,2,3,1,1,1,1,0,1,1,0,4,5]
print(count_consequtive_1s(arr))
