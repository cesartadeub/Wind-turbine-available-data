"""
parse_data.py - Wind Turbine Data Parsing and Filtering Module

This module provides functions for parsing and filtering wind turbine data.
It includes utilities for loading datasets and applying state-specific filters,
particularly for Iowa-specific wind turbine data analysis.
"""

import pandas as pd


def parse_wind_turbine_data(filepath):
    """Parse wind turbine data from a CSV file.

    Args:
        filepath (str): Path to the CSV file containing wind turbine data.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the parsed wind turbine data.
    """
    df = pd.read_csv(filepath)
    return df


def filter_iowa_data(df):
    """Filter a wind turbine DataFrame to include only Iowa (IA) records.

    This function filters the input DataFrame to return only the rows where
    the 'state' column equals 'IA', corresponding to Iowa-specific wind
    turbine data. This is useful for conducting Iowa-focused wind energy
    efficiency analyses.

    Args:
        df (pd.DataFrame): A pandas DataFrame containing wind turbine data
            with a 'state' column that uses two-letter US state abbreviations.

    Returns:
        pd.DataFrame: A DataFrame containing only rows where the 'state'
            column equals 'IA' (Iowa). Returns an empty DataFrame if no
            Iowa records are present.

    Example:
        >>> data = pd.DataFrame({"state": ["IA", "TX", "IA", "CA"], "capacity": [100, 200, 150, 300]})
        >>> iowa_data = filter_iowa_data(data)
        >>> len(iowa_data)
        2
    """
    return df[df['state'] == 'IA']


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        data = parse_wind_turbine_data(sys.argv[1])
        print(f"Loaded {len(data)} records.")
        iowa = filter_iowa_data(data)
        print(f"Found {len(iowa)} Iowa records.")
    else:
        print("Usage: python parse_data.py <csv_filepath>")
