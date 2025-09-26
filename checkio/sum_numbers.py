def sum_numbers(text: str) -> int:
    number = []
    text_split = text.split()
    
    for element in text_split :
        if element.isnumeric() == True :
            number.append(int(element))
    return sum(number)