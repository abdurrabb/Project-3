import pandas as pd
from collections import defaultdict

def filter_olympic(dataframe, target_column = 'school', false_numerics=[], unique_identifiers=[]):
    dataframe = dataframe.copy()
    olympic = dataframe.loc[dataframe[target_column].str.contains('Olympic')].copy()
    for column in false_numerics:
        olympic[column] = olympic[column].apply(lambda x: str(x))
    olympic['key'] = ''
    for identifier in unique_identifiers:
        olympic['key'] =  olympic['key'] + olympic[identifier]
    olympic.set_index('key', inplace=True)
    new_olympic = defaultdict(dict)
    for label, content in olympic.items():
        i = 0
        for item in content:
            key = content.index[i]
            if type(item) == int:
                if label in new_olympic[key].keys():
                    new_olympic[key][label] += item
                else:
                    new_olympic[key][label] = item
            else:
                new_olympic[key][label] = item
                new_olympic[key][target_column] = "Olympic High"
            i += 1
    dataframe_out = dataframe[dataframe[target_column].str.contains('Olympic') == False]
    dataframe_out = dataframe_out.append(list(new_olympic.values()))
    return dataframe_out