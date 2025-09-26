import pandas as pd
import operator


def most_frequent(data: list[str]) -> str:

    unique_dict = dict.fromkeys(data)
    for element in unique_dict.keys() :
        unique_dict[element] = data.count(element)
    return max(unique_dict.items(), key=operator.itemgetter(1))[0]