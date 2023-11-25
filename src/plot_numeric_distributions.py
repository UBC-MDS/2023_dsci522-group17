## Modularized Visualization function

import os
import numpy as np
import altair as alt
import pandas as pd


def plot_numeric_distributions(data, target, numeric_features=None, stack_order=None):
    """
    Plot histograms for all numeric features in the dataset.

    Parameters
    ----------
    - data : DataFrame
        the dataset
    - target : str
        name of the target variable
    - numeric_features : {'None', 'list'}, optional
        list of names of the numeric features, by default 'None'

    Returns
    -------
    object
        alt.Chart
        
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError('dataset must be a DataFrame') 

    if not isinstance(target, str):
        raise TypeError('target variable must be of type string') 
    
    if numeric_features == None:
        numeric_features = np.array(data.select_dtypes(include=['float64', 'int64']).columns)
    else:
        # Test: Check whether input list is of type 'list'
        if not isinstance(numeric_features, list):
            raise TypeError('numeric_features must be a list') 

        # Check to make sure the elements of numeric_features are of datatype string
        for element in numeric_features:
            if not isinstance(element, str):
                raise ValueError("numeric_feats must contain only string elements")


    # Creating the repeated altair plot
    final_plots = alt.Chart(data).mark_bar(opacity=0.3).encode(
        alt.X(alt.repeat()).type('quantitative').bin(maxbins=20),
        alt.Y('count()', stack=None).title('Frequency of Occurrence'),
        alt.Color(target).title(target).scale(scheme='viridis')
    ).properties(
        width = 150,
        height = 150
    ).repeat(
        numeric_features,
        columns = 4
    )
    return final_plots