

def preprocessor(passthrough_feats, numeric_feats):
    fifa_preprocessor = make_column_transformer(
    ("passthrough", passthrough_feats),
    (StandardScaler(), numeric_feats), 
    )
    return fifa_preprocessor