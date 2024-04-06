def find_uniq(arr):
    #iterate through array and find different number
    base = arr[0]
    for i in arr:
        #Check if unique is in first position
        if arr[0] != arr[2] and arr[0] != arr[1]:
            return arr[0]
        #Else check the position of the unique value
        elif i != base:
            return i
