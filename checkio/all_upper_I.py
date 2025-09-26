def is_all_upper(text: str) -> bool:
    if text == "" or text.isnumeric == True :
        return True
    else :
        for element in text :
            if element.islower() == True :
                return False
    return True