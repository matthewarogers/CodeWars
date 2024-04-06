def bouncing_ball(h, bounce, window):
    #Set Parameters
    count = 0
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while h > window:
            h = (h * bounce)
            count+=1
        return count * 2 -1
        
        
    else:
        return -1
