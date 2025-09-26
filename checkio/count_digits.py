def count_digits(text: str) -> int:
    
    ct = 0
    for element in text :
        if element.isnumeric() == True :
            ct = ct + 1
    return ct