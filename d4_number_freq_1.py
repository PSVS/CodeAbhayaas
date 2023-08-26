#Finding the number frequency 1
def frequency_one(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [4, 2, 3, 2, 3]
print(frequency_one(arr))
