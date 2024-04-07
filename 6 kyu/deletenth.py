def delete_nth(order,max_e):
    
    #Create new list to store values
    list = []
    
    #Iterate through order, if value is not in list for max_e, append to answer list.
    for i in order:
        if list.count(i) < max_e:
            list.append(i)
            
    return list
