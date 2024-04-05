def printer_error(s):
    #Establish noncolor letters, create list from input, create error counter
    noncolors = 'nopqrstuvwxyz'
    count = 0
    
    #iterate through input, check for noncolors
    for i in s:
        if i in noncolors:
            count+=1
            
    return(str(count) + '/' + str(len(s)))
