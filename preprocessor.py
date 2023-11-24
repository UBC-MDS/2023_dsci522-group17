import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler

# Create the function to modularize the preprocessor block
def preprocessor(passthrough_feats, numeric_feats):
    """Takes lists of numeric and passthrough"""
    fifa_preprocessor = make_column_transformer(
    ("passthrough", passthrough_feats),
    (StandardScaler(), numeric_feats), 
    )
    return fifa_preprocessor

# Create test data to test the function

test_data = pd.DataFrame({
    'num_col_1': [1, 2, 3, 4, 5],
    'num_col_2': [6, 7, 8, 9, 10],
    'pass_col_1': ['jake', 'merete', 'simon', 'waleed', 'tiffany'],
    'num_col_3': [100, 200, 300, 400, 500]
})

#Create test cases



