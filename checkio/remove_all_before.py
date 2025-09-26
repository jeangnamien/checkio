def remove_all_before(items: list, border: int) :
    
    if border not in items :
        return items
    
    elif items == [] :
        return items
    
    else :
        index = items.index(border)
        return items[index:]