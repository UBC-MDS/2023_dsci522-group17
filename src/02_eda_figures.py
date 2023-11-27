# python src/02_eda_figures.py --dataset=data/processed/fifa_train.csv --target=potential

import click
import os
import numpy as np
import altair as alt
import pandas as pd
from plot_numeric_distributions import plot_numeric_distributions

@click.command()
@click.option('--dataset', type=str)
@click.option('--target', type=str)
def main(dataset, target):
    """EDA plots"""
    # Exploratory data analysis and visualizing numeric feature distributions across classes
    dataset = pd.read_csv(dataset).set_index('Unnamed: 0')
    eda_plots = plot_numeric_distributions(dataset, target)
    eda_plots.save('results/eda_plots.png')
    
if __name__ == '__main__':
    main()
