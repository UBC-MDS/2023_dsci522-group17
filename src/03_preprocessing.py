import click
from preprocessor import preprocessor
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler


@click.command()
@click.option('--train', type=str)
@click.option('--test', type=str)
def main(train, test):
    """Preprocessing"""
    # Pre-processing
    passthrough_feats = ["potential"]
    numeric_feats = ['value_eur', 'wage_eur', 'age', 'height_cm', 'weight_kg',
        'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling',
        'defending', 'physic']

    # Creating the Column Transformer
    fifa_preprocessor = preprocessor(passthrough_feats, numeric_feats)

    train = pd.read_csv(train, index_col=0)
    test = pd.read_csv(test, index_col=0)

    fifa_preprocessor.fit(train)
    scaled_fifa_train = fifa_preprocessor.transform(train)
    scaled_fifa_test = fifa_preprocessor.transform(test)

    column_names = (passthrough_feats + numeric_feats)
    scaled_fifa_train = pd.DataFrame(scaled_fifa_train, columns=column_names)
    scaled_fifa_test = pd.DataFrame(scaled_fifa_test, columns=column_names)

    # Saving scaled data
    scaled_fifa_train.to_csv("data/processed/scaled_fifa_train.csv")
    scaled_fifa_test.to_csv("data/processed/scaled_fifa_test.csv")

if __name__ == '__main__':
    main()