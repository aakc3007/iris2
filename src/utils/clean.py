print('cleaning data')

import pandas as pd


def read_df(read_path):
    df = pd.read_csv(read_path)
    return df
    

def save_df(df, save_path):
    df.to_csv(save_path, index=False)
