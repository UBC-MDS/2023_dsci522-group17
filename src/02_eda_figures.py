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
    eda_plots = plot_numeric_distributions(dataset, target)
    eda_plots
if __name__ == '__main__':
    main()