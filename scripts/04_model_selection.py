import click
import warnings

import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.cross_val_by_model import cross_val_by_model

warnings.filterwarnings("ignore", category=FutureWarning)


@click.command()
@click.option("--scaled_train", type=str)
def main(scaled_train):
    """
    Generate and compare various models with cross validation. 
    Select best model based on performance.
    Models tested are dummy, decision KNN, RBF SVM, Naive Bayes,
    Logistic Regression.
    Save results of CV to .csv

    Parameters
    ----------
    scaled_train : string
        relative filepath to the scaled train dataset

    Outputs
    -------
    results/tables/model_cross_val_scores.csv
        aggregated cross validation results for various models

    Example
    -------
    python src/04_model_selection.py \
        --scaled_train=data/processed/scaled_fifa_train.csv
    """
    # Separating target from other features
    scaled_train = pd.read_csv(scaled_train, index_col=0)
    X_train = scaled_train.drop(columns=["potential"])
    y_train = scaled_train["potential"]

    # Set models to be tested
    models = {
        "dummy": DummyClassifier(random_state=123),
        "Decision Tree": DecisionTreeClassifier(random_state=123),
        "KNN": KNeighborsClassifier(),
        "RBF SVM": SVC(random_state=123),
        "Naive Bayes": GaussianNB(),
        "Logistic Regression": LogisticRegression(
            max_iter=2000, multi_class="ovr", random_state=123
        ),
    }

    # Conducting cross validation for each possible model
    results = cross_val_by_model(models, X_train, y_train)
    results.to_csv("results/tables/model_cross_val_scores.csv")


if __name__ == "__main__":
    main()
