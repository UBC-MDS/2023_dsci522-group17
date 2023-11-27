import click
from download_unpack_zip_extract_csv import download_unpack_zip_extract_csv 
import os
import requests
import zipfile

import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.option('--url', type=str)
@click.option('--filename', type=str)
def main(url, filename):

    """Loads our data, cleans it, splits it"""
    # Downloading and extracting the relevant file
    # url = "https://sports-statistics.com/database/fifa/fifa_2022_datasets.zip"
    # filename = "players_22.csv"
    df_raw = download_unpack_zip_extract_csv(url, filename, path="data")

    # Selecting columns for analysis
    df_processed = df_raw.loc[:, ["potential",
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
                                "physic",]]

    # Dropping observations with missing values
    df_processed = df_processed.dropna()

    # Binning the target class 'potential' into 4 categories
    df_processed['potential'] = pd.cut(x=df_processed['potential'], bins=[0, 67, 71, 75, 100], 
                        labels=['Low', 'Medium', 'Good', 'Great'])
    df_processed

    # Create the split
    fifa_train, fifa_test = train_test_split(df_processed, test_size=0.3, random_state=123)

    fifa_train.to_csv("data/processed/fifa_train.csv")
    fifa_test.to_csv("data/processed/fifa_test.csv")


if __name__ == '__main__':
    main()


