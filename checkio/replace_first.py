def replace_first(items: list) :
    if items == [] :
        return items
    else: 
        tmp = items[-1]
    items[-1] = items[0]
    items.remove(items[0])
    items.insert(-1, tmp)
    return items 