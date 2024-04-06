def sum_two_smallest_numbers(numbers):
    
    #Sort numbers list by value
    numbers.sort()
    
    #Remove any negative numbers from list
    for i in numbers:
        if i < 0:
            numbers.remove(i)

    #Truncate list to the first two values        
    n = len(numbers)
    k = 2
    for i in range(0, n - k):
        numbers.pop()
        
    return sum(numbers)
