import pytest
import os
import sys
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
import warnings

warnings.filterwarnings("ignore")

# Import cross_val_by_model() from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.cross_val_by_model import cross_val_by_model

# Test data setup

# First test case:
model_dict1 = {
    "RBF SVM": SVC(random_state=123),
}
X_train1 = pd.DataFrame(np.ones((200, 1))).rename(columns={0: "feature"})
y_train1 = pd.DataFrame([["yes"] * 100 + ["no"] * 100]).T.rename(columns={0: "target"})
results1 = cross_val_by_model(model_dict1, X_train1, y_train1)

# Second test case:
model_dict2 = {
    "dummy": DummyClassifier(random_state=123),
    "Decision Tree": DecisionTreeClassifier(random_state=123),
}
X_train2 = pd.DataFrame(np.zeros((200, 1))).rename(columns={0: "feature"})
y_train2 = pd.DataFrame([["yes"] * 150 + ["no"] * 50]).T.rename(columns={0: "target"})
results2 = cross_val_by_model(model_dict2, X_train2, y_train2)


# Tests


# Test that the function returns a dataframe
def test_cross_val_by_model_returns_df():
    assert isinstance(
        results1, pd.core.frame.DataFrame
    ), "cross_val_by_model() should return a pandas DataFrame"
    assert isinstance(
        results2, pd.core.frame.DataFrame
    ), "cross_val_by_model() should return a pandas DataFrame"


# Test that the dataframe is the right shape
def test_cross_val_by_model_returns_correct_shape():
    assert results1.shape == (
        4,
        len(model_dict1),
    ), "cross_val_by_model() is returning the wrong shape of DataFrame"
    assert results2.shape == (
        4,
        len(model_dict2),
    ), "cross_val_by_model() is returning the wrong shape of DataFrame"


# Test that the data in the dataframe are strings
def test_cross_val_by_model_returns_strings_in_cell():
    assert isinstance(
        results1.iloc[0, 0], str
    ), "cross_val_by_model() should return a DataFrame of strings"
    assert isinstance(
        results2.iloc[0, 0], str
    ), "cross_val_by_model() should return a DataFrame of strings"


# Test that the columns of the dataframe are the same as the keys in the model dictionary
def test_cross_val_by_model_columns_are_dictkeys():
    assert results1.columns.tolist() == list(
        model_dict1.keys()
    ), "The DataFrame's columns should be the same as the dictionary's keys"
    assert results2.columns.tolist() == list(
        model_dict2.keys()
    ), "The DataFrame's columns should be the same as the dictionary's keys"
