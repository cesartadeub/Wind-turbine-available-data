"""
parse_data.py - Wind Turbine Data Parsing Module

This module provides utilities for parsing and filtering wind turbine data.
It supports reading turbine data from various sources and applying filters
for state-specific analysis, particularly for Iowa (IA) datasets.
"""

import pandas as pd


def parse_turbine_data(filepath):
    """Parse wind turbine data from a CSV file.

    Args:
        filepath: Path to the CSV file containing wind turbine data.

    Returns:
        A pandas DataFrame with the parsed wind turbine data.
    """
    return pd.read_csv(filepath)


def filter_iowa_data(df):
    """Filter a DataFrame to include only rows where the state is Iowa (IA).

    This function is designed to support Iowa-specific wind turbine data
    analysis by isolating records that pertain to the state of Iowa. It
    filters the input DataFrame based on the 'state' column, returning
    only rows where the state code equals 'IA'.

    Args:
        df: A pandas DataFrame that must contain a 'state' column.

    Returns:
        A pandas DataFrame containing only the rows where the 'state'
        column equals 'IA'.

    Raises:
        KeyError: If the 'state' column is not present in the DataFrame.

    Example:
        >>> df = pd.DataFrame({"state": ["IA", "TX", "IA", "CA"], "capacity": [100, 200, 150, 300]})
        >>> filter_iowa_data(df)
          state  capacity
        0    IA       100
        2    IA       150
    """
    if "state" not in df.columns:
        raise KeyError("DataFrame must contain a 'state' column.")
    return df[df["state"] == "IA"]


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse_data.py <csv_filepath>")
        sys.exit(1)

    data = parse_turbine_data(sys.argv[1])
    iowa_data = filter_iowa_data(data)
    print(f"Total records: {len(data)}")
    print(f"Iowa records: {len(iowa_data)}")
