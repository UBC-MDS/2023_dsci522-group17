# Imports
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

def cross_val_by_model(model_dict, X_train, y_train, **kwargs):
    #Returns a data frame of cross-validation scores for each model passed to the function in a dictionary.

    #Parameters:
    #   model_dict (dict): A dictionary containing models to be run.
    #   It should have the following key-value pairs:
    #   - 'name': (str) The name of the model
    #   - 'X': (idk) code initializing the model    

    #Returns:
    #    results (pd.DataFrame): A dataframe containing the resulf from the cross-validation  

    results = pd.DataFrame()
    for name, model in model_dict.items():
        scores = cross_validate(model, X_train, y_train, return_train_score=True)

        mean_scores = pd.DataFrame(scores).mean()
        std_scores = pd.DataFrame(scores).std()
        out_col = []

        for i in range(len(mean_scores)):
            out_col.append((f"%0.3f (+/- %0.3f)" % (mean_scores[i], std_scores[i])))

        
        results[name] = pd.Series(data=out_col, index=mean_scores.index)
    return results
