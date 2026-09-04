#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Wind Turbine Data Parsing Utilities

This module provides utility functions for parsing and filtering
wind turbine SCADA datasets. It includes general data loading
functions as well as location-specific filter helpers.

Functions:
    load_data(filepath) - Load wind turbine data from CSV file
    filter_iowa_data(df) - Filter DataFrame to only Iowa (IA) state rows
"""

import pandas as pd


def load_data(filepath):
    """
    Load wind turbine data from a CSV file.

    Parameters
    ----------
    filepath : str
        Path to the CSV file containing wind turbine data.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the loaded wind turbine data.

    Examples
    --------
    >>> df = load_data('wind_turbine_data.csv')
    >>> df.head()
    """
    return pd.read_csv(filepath)


def filter_iowa_data(df):
    """
    Filter a DataFrame to return only rows where the 'state' column equals 'IA'.

    This function is specifically designed for filtering wind turbine
    datasets to include only entries from the state of Iowa (IA).

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing a 'state' column with US state codes.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame containing only rows where state == 'IA'.

    Raises
    ------
    KeyError
        If the 'state' column does not exist in the input DataFrame.

    Examples
    --------
    >>> df = pd.DataFrame({'state': ['IA', 'MN', 'IA'], 'value': [1, 2, 3]})
    >>> filter_iowa_data(df)
       state  value
    0    IA      1
    2    IA      3
    """
    if 'state' not in df.columns:
        raise KeyError("The input DataFrame must contain a 'state' column.")
    return df[df['state'] == 'IA']
