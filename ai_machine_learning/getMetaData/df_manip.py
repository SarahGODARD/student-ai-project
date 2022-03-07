import pandas as pd

def add_dict_to_df(df, dic):
    """Add a dictionary's content in a data frame and return it.
    Args:
        df (dataframe): the dataframe to fill.
        dic (dictionary): the dictionary with the data to add.

    Returns:
        dataframe: the nex filled dataframe.

    """
    for tag in dic.keys():
        res = str(dic[tag])
        res = res.replace(",", "")
        df[str(tag)] = res
    return df