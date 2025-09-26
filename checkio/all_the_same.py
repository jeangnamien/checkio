def all_the_same(elements:list) -> bool:
    for i in range(len(elements)-1) :
        if elements[i] == elements[i+1] :
            pass
        else :
            return False
    return True