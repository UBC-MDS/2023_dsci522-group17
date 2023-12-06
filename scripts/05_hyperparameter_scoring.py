import click
import pickle

import pandas as pd

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV


@click.command()
@click.option("--scaled_train", type=str)
@click.option("--scaled_test", type=str)
def main(scaled_train, scaled_test):
    """
    Perform hyperparameter tuning for the selected RBF SBM model. 
    Evaluate best performing model on test data. 
    Export results of tuning, test scores, and best model

    Parameters
    ----------
    scaled_train : string
        relative filepath to the scaled train dataset
    scaled_test : string
        relative filepath to the scaled test dataset

    Outputs
    -------
    results/hyperparameter_rankings.csv
        top 5 results of hyperparameter tuning including parameters and
        performance
    results/test_score.csv
        performance results for the best model evaluated on test data
    results/best_model.pickle
        fitted best model pickled for export

    Example
    -------
    python src/04_model_selection.py \
        --scaled_train=data/processed/scaled_fifa_train.csv
    """
    # Separating target from other features
    scaled_train = pd.read_csv(scaled_train, index_col=0)
    X_train = scaled_train.drop(columns=["potential"])
    y_train = scaled_train["potential"]

    scaled_test = pd.read_csv(scaled_test, index_col=0)
    X_test = scaled_test.drop(columns=["potential"])
    y_test = scaled_test["potential"]

    # generate parameters and search
    param_dist = {
        "svc__C": [0.001, 0.01, 0.1, 1, 10, 100],
        "svc__gamma": [0.001, 0.01, 0.1, 1, 10, 100],
    }

    pipe = make_pipeline(SVC(random_state=123))

    random_search = RandomizedSearchCV(
        pipe,
        param_dist,
        n_iter=36,
        n_jobs=-1,
        return_train_score=True,
        random_state=123,
    )

    random_search.fit(X_train, y_train)

    rankings = (
        pd.DataFrame(random_search.cv_results_)[
            [
                "mean_test_score",
                "mean_train_score",
                "param_svc__C",
                "param_svc__gamma",
                "mean_fit_time",
                "rank_test_score",
            ]
        ]
        .set_index("rank_test_score")
        .sort_index()
        .iloc[:5]
    )

    rankings.to_csv("results/hyperparameter_rankings.csv")

    # Get best_model
    best_model = random_search.best_estimator_

    # Export model to pickle
    with open("results/best_model.pickle", "wb") as f:
        pickle.dump(best_model, f)

    # Score
    score = best_model.score(X_test, y_test)
    score = pd.DataFrame(index=["SVC"], data={"Test Score": score})
    score.to_csv("results/test_score.csv")


if __name__ == "__main__":
    main()
