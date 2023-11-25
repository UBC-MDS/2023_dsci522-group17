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


# The below model is adapted from DSCI_571's mean_std_cross_val_scores() found here:
# https://pages.github.ubc.ca/MDS-2023-24/DSCI_571_sup-learn-1_students/lectures/02_ml-fundamentals.html?highlight=mean_std_cross_val_scores


def cross_val_by_model(model_dict, X_train, y_train):
    """
    Returns a data frame of cross-validation scores for
    each model passed to the function in a dictionary.

    Parameters
    ----------
    model_dict : dict
        A dictionary containing models to be run. It
        should have the following key-value pairs:
        - key: (str) the name of a model
        - value: (object) the initialization of the model
    X_train : pandas DataFrame
        A pandas dataframe of the training data without the
        target class
    y_train : pandas DataFrame
        A pandas dataframe of the target class from the
        training data

    Returns
    -------
    results
        a pandas dataframe containing the resulf from
        the cross-validation

    Raises
    ------
    TypeError
        when a the parameters passed are not the correct
        data type/instance
    """
    if not isinstance(model_dict, dict):
        raise TypeError("model_dict must be a dictionary")
    if not isinstance(list(model_dict.items())[0][0], str):
        raise TypeError("model_dict keys must be strings")
    if not isinstance(list(model_dict.items())[0][1], object):
        raise TypeError("model_dict values must be objects")
    if not isinstance(X_train, pd.core.frame.DataFrame):
        raise TypeError("X_train must be a pandas DataFrame")
    if not isinstance(y_train, pd.core.frame.DataFrame):
        raise TypeError("y_train must be a pandas DataFrame")

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
