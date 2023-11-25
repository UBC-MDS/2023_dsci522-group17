import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler

# Create the function to modularize the preprocessor block
def preprocessor(passthrough_feats, numeric_feats):
    """Takes lists of numeric and passthrough features and creates a column transformer,
    'fifa_preprocessor' that runs StandardScaler on the numeric features, and 
    passes through the passthrough features.

    Parameters
    ----------
    passthrough_feats : 
        list of passthrough feature column names

    numeric_feats :
        list of numeric feature column names

    Returns
    -------
    fifa_preprocessor
        a column transformer object
    """
    # Check to make sure both parameters are lists otherwise raise a type error
    if not isinstance(passthrough_feats, 'list'):
        raise TypeError('passthrough_feats must be a list')
    
    if not isinstance(numeric_feats, 'list'):
        raise TypeError('numeric_feats must be a list') 
    

    # Check to make sure the elements of numeric_feats are numeric
    


    # Create the column transformer
    fifa_preprocessor = make_column_transformer(
    ("passthrough", passthrough_feats),
    (StandardScaler(), numeric_feats), 
    )
    return fifa_preprocessor





