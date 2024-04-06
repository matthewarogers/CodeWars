def find_outlier(integers):
    #Create Lists to store odds and evens
    evens = []
    odds = []
    
    #Separate input by odd and even
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
            
        else:
            odds.append(i)
            
    #Return outlier        
    if len(evens) == 1:
        return evens[0]
        
    else:
        return odds[0]
