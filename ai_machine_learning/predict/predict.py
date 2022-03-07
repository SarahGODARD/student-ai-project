import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import numpy


model_path = '../model/analyserModel.sav'
file_path = './predict_analyser.csv'

def get_input(file_path):
    new_input = pd.DataFrame()
    df = pd.read_csv(file_path, engine='python')
    for e in df:
        new_input = pd.concat([pd.get_dummies(df[e]), new_input], axis=1)
    return df.to_numpy()

def print_state_prediction(prediction):
    for e in prediction:
        if int(e) == 1:
            print("It's a scam!")
        else:
            print("It is not a scam.")

def get_input_from_values(self, values):
    print(values)