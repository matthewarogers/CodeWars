def filter_list(l):
  #Create result list
    results = []

  #Iterate through input, detect if an int. If true, append to results list.
    for i in l:
        if isinstance(i,int):
            results.append(i)
            
    return results
