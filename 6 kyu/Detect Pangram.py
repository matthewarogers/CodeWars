def is_pangram(s):
    
    #Create Alphabet variable
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    #Convert string into lower case to match alphabet variable
    s = s.lower()
    
    #Create Control Variable
    b = True
    
    #Parse through alphabet variable
    for i in alphabet:
        #Check if each letter is in string, if not set control variable to false.
        if i not in s:
            b = False
    #Return Control Variable      
    return b
