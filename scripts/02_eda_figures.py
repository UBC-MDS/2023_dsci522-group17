import click
import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.plot_numeric_distributions import plot_numeric_distributions


@click.command()
@click.option("--dataset", type=str)
@click.option("--target", type=str)
def main(dataset, target):
    """
    Generate EDA plots from raw dataset and save to file
    Visualize numeric feature distribution across target classes

    Parameters
    ----------
    dataset : string
        relative filepath to the training dataset for visualization
    target : string
        the target or response variable of the analysis, categorical

    Outputs
    -------
    results/figures/eda_plots.png
        export of dataset visualizations

    Example
    -------
    python src/02_eda_figures.py \
        --dataset=data/processed/fifa_train.csv \
        --target=potential
    """
    # Read .csv and generate plot
    dataset = pd.read_csv(dataset).set_index("Unnamed: 0")

    eda_plots = plot_numeric_distributions(dataset, target)
    eda_plots.save("results/figures/eda_plots.png")


if __name__ == "__main__":
    main()
