def backward_string(val: str) -> str:
    lav = []
    i = len(val) -1
    while i >=0 :
        lav.append(f'{val[i]}')
        i-=1
    return ''.join(lav)