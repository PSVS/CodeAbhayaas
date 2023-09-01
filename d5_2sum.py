def twoSum(arr, x):
    dict = {}
    res = []
    for i in range(len(arr)):
        complement = x - arr[i]
        if complement in dict:
            res.append((i, complement))
        dict[arr[i]] = i

    return res
