"""
parse_data.py

Module for parsing and filtering wind turbine data.

This module provides utility functions for loading, parsing, and filtering
wind turbine SCADA datasets. It includes functionality to filter datasets
by geographic region, specifically for Iowa-based wind turbine data.

Functions:
    load_data: Load wind turbine data from a CSV file.
    filter_iowa_data: Filter a DataFrame to include only Iowa (IA) records.
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load wind turbine data from a CSV file.

    Args:
        filepath: Path to the CSV file containing wind turbine data.

    Returns:
        A pandas DataFrame with the loaded wind turbine data.
    """
    return pd.read_csv(filepath)


def filter_iowa_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter a DataFrame to include only rows where the state is Iowa (IA).

    This function filters the input DataFrame to return only records where
    the 'state' column equals 'IA', corresponding to Iowa. This is useful
    for isolating wind turbine data specific to Iowa for regional analysis.

    Args:
        df: A pandas DataFrame containing wind turbine data with a 'state' column.

    Returns:
        A pandas DataFrame containing only rows where the 'state' column equals 'IA'.
    """
    return df[df["state"] == "IA"]


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) > 1:
        data = load_data(sys.argv[1])
        iowa_data = filter_iowa_data(data)
        print(f"Total records: {len(data)}")
        print(f"Iowa records: {len(iowa_data)}")
    else:
        print("Usage: python parse_data.py <csv_filepath>")
