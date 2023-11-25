## Modularized Visualization function

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

    
    
    if numeric_features == None:
        numeric_features = np.array(data.select_dtypes(include=['float64', 'int64']).columns)

    final_plots = alt.Chart(data).mark_bar(opacity=0.3).encode(
        alt.X(alt.repeat()).type('quantitative').bin(maxbins=20),
        alt.Y('count()', stack=None).title(''),
        alt.Color(target).sort(stack_order).title(target).scale(scheme='viridis')
    ).properties(
        width = 150,
        height = 150
    ).repeat(
        numeric_features,
        columns = 4
    )
    return final_plots