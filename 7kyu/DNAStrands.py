def DNA_strand(dna):
    
    #created empty list to store complements.
    comp = []
    
    #iterate through input, find complement of each iteration then append it to com list.
    for i in dna:
        if i == 'A':
            comp.append('T')
        if i == 'T':
            comp.append('A')
            
        if i == 'C':
            comp.append('G')
            
        if i == 'G':
            comp.append('C')
            
    #join list into one string
    results = ''.join(comp)
    
    return results
