def number_length(value: int) -> int:

    
    
        
        i = 1
        while True :
            if (value // 10**i) == 0 :
                 return i 
            i +=1