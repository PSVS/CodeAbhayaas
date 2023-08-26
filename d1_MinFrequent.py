#Minimum Frequent Number
def MinFrequent(arr):
    hashmap = {}
    for num in arr:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    min_frequency = float('inf')
    min_number = None
    for num, count in hashmap.items():
        if count<min_frequency:
            min_frequency = count
            min_number = num
    return min_frequency


arr = [4, 2, 10, 4, 5, 2, 4]
print(MinFrequent(arr))
