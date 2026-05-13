"""
parse_data.py

Module for parsing and filtering wind turbine data.
Supports reading turbine datasets and filtering by state,
with specialized support for Iowa (IA) wind turbine data.
"""

import pandas as pd


def parse_turbine_data(filepath: str) -> pd.DataFrame:
    """Parse wind turbine data from a CSV file.

    Args:
        filepath: Path to the CSV file containing wind turbine data.

    Returns:
        A pandas DataFrame containing the parsed wind turbine data.
    """
    df = pd.read_csv(filepath)
    return df


def filter_by_state(df: pd.DataFrame, state_code: str) -> pd.DataFrame:
    """Filter a DataFrame to include only rows matching the given state code.

    Args:
        df: A pandas DataFrame with a 'state' column.
        state_code: The two-letter state code to filter by (e.g., 'IA', 'TX').

    Returns:
        A DataFrame containing only rows where the 'state' column equals the given state code.
    """
    return df[df['state'] == state_code]


def filter_iowa_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter a DataFrame to include only Iowa wind turbine data.

    This function filters the input DataFrame to return only rows where
    the 'state' column equals 'IA' (Iowa). It is designed to support
    Iowa-specific wind energy dataset compatibility and analysis.

    Args:
        df: A pandas DataFrame containing wind turbine data with a 'state' column.
            The 'state' column should contain two-letter US state codes.

    Returns:
        A pandas DataFrame containing only rows where the 'state' column equals 'IA'.

    Example:
        >>> import pandas as pd
        >>> data = pd.DataFrame({
        ...     'state': ['IA', 'TX', 'IA', 'CA'],
        ...     'turbine_capacity': [2.0, 3.5, 1.8, 4.0]
        ... })
        >>> iowa_data = filter_iowa_data(data)
        >>> len(iowa_data)
        2
    """
    return df[df['state'] == 'IA']
