def end_zeros(a: int) -> int:
    cntr = 0
    i=1
    while True :
        if a == 0:
            return 1
        if a % 10**i == 0:
            cntr +=1
        else:
            return cntr
        i +=1