"""
parse_data.py - Wind Turbine Data Parsing and Filtering Module

This module provides utilities for parsing and filtering wind turbine
SCADA datasets. It includes functions for loading data from various
sources and filtering by geographic region, with specific support for
Iowa (IA) dataset compatibility.

Supported datasets include:
- Kelmarsh Wind Farm Data
- Penmanshiel Wind Farm Data
- Canadian Wind Turbine Database
- Open Energy Data Initiative (OEDI)
- US Wind Turbine Database (USWTDB)

Usage:
    import pandas as pd
    from parse_data import filter_iowa_data

    df = pd.read_csv("us_wind_turbine_data.csv")
    iowa_df = filter_iowa_data(df)
"""

import pandas as pd


def filter_iowa_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filter a wind turbine DataFrame to include only Iowa (IA) records.

    This function filters the input DataFrame to return only rows where
    the 'state' column equals 'IA', which corresponds to Iowa in the
    United States. This is useful for Iowa-specific wind energy analyses,
    as Iowa is one of the leading wind energy producing states in the US.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame containing wind turbine data. Must include a
        'state' column with US state abbreviations (e.g., 'IA', 'TX', 'CA').

    Returns
    -------
    pd.DataFrame
        A filtered DataFrame containing only rows where the 'state' column
        equals 'IA'. The returned DataFrame is a copy of the filtered rows,
        so modifications to it will not affect the original DataFrame.

    Raises
    ------
    KeyError
        If the 'state' column is not present in the input DataFrame.

    Examples
    --------
    >>> import pandas as pd
    >>> from parse_data import filter_iowa_data
    >>> data = {
    ...     'turbine_id': [1, 2, 3, 4],
    ...     'state': ['IA', 'TX', 'IA', 'CA'],
    ...     'capacity_mw': [2.0, 3.5, 1.8, 2.5]
    ... }
    >>> df = pd.DataFrame(data)
    >>> iowa_df = filter_iowa_data(df)
    >>> print(iowa_df)
       turbine_id state  capacity_mw
    0           1    IA          2.0
    2           3    IA          1.8
    """
    if 'state' not in df.columns:
        raise KeyError(
            "The input DataFrame must contain a 'state' column. "
            f"Available columns: {list(df.columns)}"
        )

    return df[df['state'] == 'IA'].copy()


if __name__ == "__main__":
    # Example usage with sample data
    sample_data = {
        'turbine_id': [1, 2, 3, 4, 5],
        'state': ['IA', 'TX', 'IA', 'CA', 'IA'],
        'capacity_mw': [2.0, 3.5, 1.8, 2.5, 4.0],
        'year_installed': [2015, 2018, 2016, 2020, 2019],
    }
    df = pd.DataFrame(sample_data)
    iowa_df = filter_iowa_data(df)
    print("Original DataFrame:")
    print(df)
    print("\nIowa-filtered DataFrame:")
    print(iowa_df)