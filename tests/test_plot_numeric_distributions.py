import pandas as pd
import pytest
import sys
import os
import altair as alt
import numpy as np

# Import the plot_numeric_distributions function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.plot_numeric_distributions import plot_numeric_distributions

## Sample Dataset
sample_data = pd.DataFrame({
    'Age': [25, 25, 25, 30, 35, 40, 45],
    'Income': [50000, 50000, 50000, 60000, 75000, 90000, 100000],
    'Score': [80, 85, 75, 65, 90, 92, 88],
    'Target': ['good', 'bad', 'good', 'good', 'bad', 'bad', 'bad'],
    'Laugh': ['haha', 'hahahah', 'aha', 'hahahah', 'aha', 'hahahah', 'aha']
})


# Test: Check if the output is the correct altair object
def test_graph_type():
    assert isinstance(plot_numeric_distributions(sample_data, 'Target'), alt.RepeatChart), "The chart created is of the wrong type and is not a RepeatChart object."

# Test: Check that the y-axis type is correct
def test_y_axis_type():
    assert plot_numeric_distributions(sample_data, 'Target').to_dict()["spec"]["encoding"]["y"]["aggregate"] == "count", "The y axis is not a count of the x-values."
    assert plot_numeric_distributions(sample_data, 'Target').to_dict()["spec"]["encoding"]["y"]["type"] == "quantitative", "The y axis is not of type quantitative."

# Test: Check if the altair RepeatChart object created only has graphs for the numeric features in the DataFrame
def test_repeat_features():
    assert plot_numeric_distributions(sample_data, 'Target').to_dict()["repeat"] == ["Age", "Income", "Score"], "The wrong columns are being repeated in the RepeatChart object."




