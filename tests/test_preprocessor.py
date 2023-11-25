import pytest
import pandas as pd
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.preprocessor import preprocessor

# Create test data to test the function
test_data = pd.DataFrame({
    'num_col_1': [1, 2, 3, 4, 5],
    'num_col_2': [6, 7, 8, 9, 10],
    'pass_col_1': ['jake', 'merete', 'simon', 'waleed', 'tiffany'],
    'num_col_3': [100, 200, 300, 400, 500]
})

# Create passthrough_feats and numeric_feats
passthrough_feats = ['pass_col_1']
numeric_feats = ['num_col_1', 'num_col_2', 'num_col_3']


# Tests

# Test to make sure function returns a column transformer object
def test_create_columntransformer():
    preprocessor(passthrough_feats, numeric_feats)
    assert isinstance(fifa_preprocessor, ColumnTransformer)



