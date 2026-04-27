"""
parse_data.py
=============

Module for parsing and filtering wind turbine SCADA dataset data.

This module provides utility functions for loading, parsing, and filtering
wind turbine data from various open source datasets. It includes support
for Iowa-specific data filtering to support regional wind energy analysis.

Functions:
    - load_data: Load wind turbine data from a CSV file into a pandas DataFrame.
    - filter_iowa_data: Filter the DataFrame to include only Iowa (IA) records.
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load wind turbine data from a CSV file into a pandas DataFrame.

    Args:
        filepath: Path to the CSV file containing wind turbine data.

    Returns:
        A pandas DataFrame with the loaded wind turbine data.
    """
    df = pd.read_csv(filepath)
    return df


def filter_iowa_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter the DataFrame to include only rows where the state is Iowa (IA).

    This function is designed to support Iowa-specific wind energy analysis
    by filtering a wind turbine dataset to only include records from the
    state of Iowa. The input DataFrame must contain a 'state' column with
    two-letter US state abbreviations.

    Args:
        df: A pandas DataFrame containing wind turbine data with a 'state' column.

    Returns:
        A pandas DataFrame containing only rows where the 'state' column equals 'IA'.

    Example:
        >>> df = pd.DataFrame({
        ...     'state': ['IA', 'TX', 'IA', 'CA'],
        ...     'turbine_capacity': [2.0, 3.5, 1.8, 4.0]
        ... })
        >>> iowa_df = filter_iowa_data(df)
        >>> len(iowa_df)
        2
    """
    return df[df['state'] == 'IA']
