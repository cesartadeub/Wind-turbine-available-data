# Utility functions for parsing wind turbine datasets

"""
Utility functions for parsing wind turbine datasets.
"""

import pandas as pd

def filter_iowa_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the given DataFrame to only include rows where the ``state`` column
    is equal to ``"IA"`` (Iowa).

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing a ``state`` column.

    Returns
    -------
    pd.DataFrame
        A DataFrame with only rows from Iowa.
    """
    if 'state' not in df.columns:
        raise KeyError("The DataFrame does not contain a 'state' column.")
    return df[df['state'] == 'IA']
