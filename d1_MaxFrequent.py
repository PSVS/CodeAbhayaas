#Maximum Frequent
def MaxFrequent(arr):
    hashmap = {}
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    max_frequency = float('-inf')
    max_number = None
    for num, count in hashmap.items():
        if count>max_frequency:
            max_frequency = count
            max_number = num
    return max_frequency


arr = [4, 2, 10, 4, 5, 2, 4]
print(MaxFrequent(arr))
