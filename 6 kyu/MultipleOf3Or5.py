def solution(number):
    #Create List for multiples
    num = []
    
    #Iterate through the range from 0 to number, if non-negative and a multiple of 3 or 5 append to num.
    for i in range(0,number):
        if i % 3 == 0 and i > 0 or i % 5 == 0 and i > 0:
            num.append(i)
            
    return sum(num)
