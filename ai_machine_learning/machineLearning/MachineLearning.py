from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import sklearn
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

from sklearn.datasets import load_iris
from sklearn.tree import export_graphviz

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor


# rfc = RandomForestClassifier(random_state=42)
# rfc.fit(X_train, y_train)

# change those values to handle other file and folders
df_file_path = '../dataCsv/data.csv'
feature_path ='../metaDataCsv/feature.csv'
model_path = '../model/analyserModel.sav'

# Create the right test and train data
def handle_meataData(file_path, size, rstate, shuf, strat, output_tag):
    new_input = pd.DataFrame()
    new_output = pd.DataFrame()
    df = pd.read_csv(file_path, engine='python')
    # Split the data into input and output
    result = df[output_tag]
    print("result: ", result)
    features = df.drop([output_tag], axis=1)
    print("features:", features)
    le = sklearn.preprocessing.LabelEncoder()
    # handling string inputs and ouputs
    new_input.to_csv(feature_path, index = False, header=True)
    new_output = np.asarray(result)
    new_input = np.asarray(features)
    # new_input = new_input.to_numpy()
    print("Shape of the trainig input dataset : ", new_input.shape)
    print(new_input)
    print("Shape of the trainig output dataset : ", new_output.shape)
    print(new_output)
    input_train, input_test, output_train, output_test = train_test_split(new_input, new_output, test_size=size, random_state=None, shuffle=None, stratify=None)
    return {"input_train": input_train, "input_test": input_test, "output_train":output_train, "output_test": output_test}

# Find best param. Must be used instead of train and test
def tune_rf_hyperparam(train):
    n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    max_features = ['auto', 'sqrt']
    max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
    max_depth.append(None)
    min_samples_split = [2, 5, 10]
    min_samples_leaf = [1, 2, 4]
    bootstrap = [True, False]
    random_grid = {
            'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap
               }

    rf = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid)
    rf_random.fit(train["input_train"], train["output_train"].ravel())
    print("Best Param : ")
    print(rf_random.best_params_)
    return rf_random.best_estimator_

# Create a random forest model and return it
def create_randomForestClassifier():
    rf = RandomForestClassifier(n_jobs=2, random_state=0)
    print("Parameters currently in use : ")
    print(rf.get_params())
    return rf

# Training the model with the data passed as parameter
def train_RF_model(model, train):
    print(train["input_train"], train["output_train"].ravel())
    model.fit(train["input_train"], train["output_train"].ravel())

def display_results(train, pred):
    plt.ylim(0, 100)
    plt.plot(train['output_test'], label="test")
    plt.plot(pred, label="train")
    plt.show()
    plt.savefig('results.png')

def dispay_random_forest(model):
    iris = load_iris()
    # model = RandomForestClassifier(n_estimators=10)

    # Train
    # model.fit(iris.data, iris.target)
    # Extract single tree
    estimator = model.estimators_[5]

    # Export as dot file
    dot_data = export_graphviz(estimator, out_file='tree.dot', 
                    feature_names = ["nb_occurence","desc_intent","desc_sentiment","desc_mistakes","title_match","title_intent","title_sentiment","title_mistakes"],
                    rounded = True, proportion = False, 
                    precision = 2, filled = True)

    # Convert to png using system command (requires Graphviz)
    from subprocess import call
    call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

    # Display in jupyter notebook
    from IPython.display import Image
    Image(filename = 'tree.png')

# Test the model and get the accuracy
def test_RF_model(model, train):
    print("INPUT TESt",train["input_test"])
    pred = model.predict(train["input_test"])
    f = open("result.txt", "w")
    ##print("The accuracy is :", int(accuracy_score(train['output_test'].ravel(), pred)*100), "%")
    # f.write("result of the training\nFalse/True\n" + str(pred) +"\nInstead of\n" + str(train["output_test"]) +"\nAccuracy : " + str(accuracy_score(train['output_test'], pred, normalize=False)) + "%")
    print("Prediction :", pred)
    print("Real result :", train['output_test'].ravel())
    display_results(train, pred)
    dispay_random_forest(model)


# save the model. Name of the file at the top of the code
def save_model(model):
    pickle.dump(model, open(model_path, 'wb'))

if __name__ == "__main__":
    print("Getting the training data...")
    train = handle_meataData(df_file_path, 0.2, None, None, None, "state")
    print("Training the model...")
    model = tune_rf_hyperparam(train)
    print("Saving the model...")
    save_model(model)
    print("Testing the model...")
    test_RF_model(model, train)
    print("The program ended well.")
