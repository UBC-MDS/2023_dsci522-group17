import click
from cross_val_by_model import cross_val_by_model

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


@click.command()
@click.option('--scaled_train', type=str)
def main(scaled_train):
    """Simple program that adds two numbers."""
    # Separating target from other features
    scaled_train = pd.read_csv(scaled_train, index_col=0)
    X_train = scaled_train.drop(columns = ['potential'])
    y_train = scaled_train['potential']

    # Looking for the best model for our data
    models = {
        "dummy": DummyClassifier(random_state=123), 
        "Decision Tree": DecisionTreeClassifier(random_state=123),
        "KNN": KNeighborsClassifier(),
        "RBF SVM": SVC(random_state=123),
        "Naive Bayes": GaussianNB(),
        "Logistic Regression": LogisticRegression(max_iter=2000, multi_class="ovr", random_state=123),
    }

    # Conducting cross validation for each possible model
    results = cross_val_by_model(models, X_train, y_train)
    results.to_csv("results/model_cross_val_scores.csv")

if __name__ == '__main__':
    main()