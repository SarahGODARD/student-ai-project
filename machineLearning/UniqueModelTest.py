import pickle
import pandas as pd
import sklearn
import numpy as np
from sklearn.metrics import r2_score
from MachineLearning import display_results
from MachineLearning import dispay_random_forest
from sklearn.metrics import mean_squared_error
import os

# change those values to handle other file and folders
df_file_path = '../dataCsv/data.csv'
feature_path ='../metaDataCsv/feature.csv'
model_path = '../model/analyserModel.sav'
directory = '../model/'

# Create the right test and train data
def handle_test_data(file_path, size, rstate, shuf, strat, output_tag):
    new_input = pd.DataFrame()
    new_output = pd.DataFrame()
    df = pd.read_csv(file_path, engine='python')
    # Split the data into input and output
    result = df[output_tag]
    features = df.drop([output_tag], axis=1)
    le = sklearn.preprocessing.LabelEncoder()
    # handling string inputs and ouputs
    new_input.to_csv(feature_path, index = False, header=True)
    new_output = np.asarray(result)
    new_input = np.asarray(features)
    # new_input = new_input.to_numpy()
    print("Shape of the trainig input dataset : ", new_input.shape)
    print("Shape of the trainig output dataset : ", new_output.shape)
    return {"input_test": new_input, "output_test": new_output}

# get the model
def get_my_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

# Test the model and get the accuracy
def test_model(model, data):
    pred = model.predict(data["input_test"])
    f = open("result.txt", "w")
    print("R2 score is :", r2_score(data['output_test'].ravel(), pred) * 100, "%")
    print("Mean square error is :", mean_squared_error(data['output_test'].ravel(), pred))
    display_results(data, pred)

def getFileList():
    return os.listdir(directory)

if __name__ == "__main__":
    print("Getting file list...")
    fileList = getFileList()
    print("Testing models...")
    for fileName in fileList:
        print("Model :", fileName)
        model = get_my_model(directory + fileName)
        data = handle_test_data(df_file_path, 0.2, None, None, None, "state")
        test_model(model, data)
    print("The program ended well.")