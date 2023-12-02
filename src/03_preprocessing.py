import click
import pandas as pd
from preprocessor import preprocessor


@click.command()
@click.option("--train", type=str)
@click.option("--test", type=str)
def main(train, test):
    """
    Preprocess data for subsequent model selection and optimization.
    Export data to .csv.

    Parameters
    ----------
    train : string
        relative filepath to the train dataset
    test : string
        relative filepath to the test dataset

    Outputs
    -------
    data/processed/scaled_fifa_train.csv
        export of scaled training data in .csv format
    data/processed/scaled_fifa_test.csv
        export of scaled test data in .csv format

    Example
    -------
    python src/03_preprocessing.py \
        --train=data/processed/fifa_train.csv \
        --test=data/processed/fifa_test.csv
    """
    # Pre-processing features
    passthrough_feats = ["potential"]
    numeric_feats = [
        "value_eur",
        "wage_eur",
        "age",
        "height_cm",
        "weight_kg",
        "weak_foot",
        "skill_moves",
        "pace",
        "shooting",
        "passing",
        "dribbling",
        "defending",
        "physic",
    ]

    # Creating the Column Transformer
    fifa_preprocessor = preprocessor(passthrough_feats, numeric_feats)

    train = pd.read_csv(train, index_col=0)
    test = pd.read_csv(test, index_col=0)

    fifa_preprocessor.fit(train)

    # transform data and assign to dataframe
    column_names = passthrough_feats + numeric_feats
    scaled_fifa_train = pd.DataFrame(
        fifa_preprocessor.transform(train), columns=column_names
    )
    scaled_fifa_test = pd.DataFrame(
        fifa_preprocessor.transform(test), columns=column_names
    )

    # export scaled data
    scaled_fifa_train.to_csv("data/processed/scaled_fifa_train.csv")
    scaled_fifa_test.to_csv("data/processed/scaled_fifa_test.csv")


if __name__ == "__main__":
    main()
