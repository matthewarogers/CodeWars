def find_uniq(arr):
    #iterate through array and find different number
    base = arr[0]
    for i in arr:
        if i != base:
            return i
