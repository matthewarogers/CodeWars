import math
def persistence(n):
    #Establish counter
    count = 0
    #check if single digit already
    if n < 10:
        return 0

    #loop through with multiplications until single digit is found
    else:
        while n >= 10:
            list = [int(i) for i in str(n)]
            n = math.prod(list)
            count += 1
        return count
