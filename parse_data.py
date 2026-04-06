
def filter_iowa_data(df):
    """Filter the DataFrame to include only rows from the state of Iowa.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing wind turbine data with a 'state' column.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing only rows where the 'state' column is 'IA'.
    """
    return df[df['state'] == 'IA']
