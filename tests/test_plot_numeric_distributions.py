import pandas as pd
import pytest
import sys
import os

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