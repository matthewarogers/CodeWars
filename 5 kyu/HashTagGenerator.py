def generate_hashtag(s):
  #Capitalize first letter of each word
    s = s.title()

  #Check if s is empty
    if s == '':
        return False
    
    #Create the hashtag
    b = '#' + s.replace(' ', '')

    #Check if length of hashtag is larger than 140
    if len(b) > 140:
        return False

    #if all conditions met, return hashtag
    else:
        return b
