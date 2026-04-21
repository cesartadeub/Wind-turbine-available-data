"""Utility module for parsing wind turbine data.

This module provides functions to process and filter data for analysis.
"""

import pandas as pd

def filter_iowa_data(df):
    """Filter the DataFrame to only include rows where the 'state' column equals 'IA'.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing a 'state' column.

    Returns
    -------
    pandas.DataFrame
        DataFrame filtered to rows with state 'IA'.
    """
    return df[df['state'] == 'IA']
