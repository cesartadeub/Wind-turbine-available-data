"""Parse wind turbine data from various sources.

This module provides utilities for reading, cleaning, and transforming
wind turbine operational data into a standardized format suitable for
analysis and visualization.
"""

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union


def parse_csv(filepath: Union[str, Path], encoding: str = "utf-8") -> List[Dict[str, str]]:
    """Parse a CSV file and return a list of row dictionaries.

    Args:
        filepath: Path to the CSV file to read.
        encoding: Character encoding to use when opening the file.

    Returns:
        A list of dictionaries, one per row, with column headers as keys.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        csv.Error: If the file contains malformed CSV data.
    """
    rows = []
    with open(filepath, mode="r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def parse_json(filepath: Union[str, Path], encoding: str = "utf-8") -> dict:
    """Parse a JSON file and return the deserialized data.

    Args:
        filepath: Path to the JSON file to read.
        encoding: Character encoding to use when opening the file.

    Returns:
        The parsed JSON data (dict, list, or primitive depending on content).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(filepath, mode="r", encoding=encoding) as f:
        return json.load(f)


def normalize_timestamp(value: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[str]:
    """Normalize a timestamp string to ISO 8601 format.

    Args:
        value: The raw timestamp string to normalize.
        fmt: The strptime format that matches the input string.

    Returns:
        An ISO 8601 formatted datetime string, or None if parsing fails.
    """
    try:
        dt = datetime.strptime(value.strip(), fmt)
        return dt.isoformat()
    except (ValueError, AttributeError):
        return None


def clean_numeric(value: str) -> Optional[float]:
    """Convert a string value to a float, handling common data issues.

    Strips whitespace and replaces comma decimal separators before
    attempting conversion. Returns None for empty or invalid values.

    Args:
        value: The string representation of a number.

    Returns:
        The float value, or None if the string cannot be converted.
    """
    if not value or not value.strip():
        return None
    try:
        return float(value.strip().replace(",", "."))
    except ValueError:
        return None


def extract_turbine_records(
    filepath: Union[str, Path],
    turbine_id_col: str = "turbine_id",
    power_col: str = "power_output_kw",
    wind_speed_col: str = "wind_speed_ms",
    timestamp_col: str = "timestamp",
) -> List[Dict[str, Union[str, float, None]]]:
    """Extract and clean turbine records from a CSV data file.

    Reads the CSV, normalizes timestamps, and converts numeric columns
    to floats, producing a list of cleaned record dictionaries.

    Args:
        filepath: Path to the source CSV file.
        turbine_id_col: Name of the column containing the turbine identifier.
        power_col: Name of the column containing power output in kW.
        wind_speed_col: Name of the column containing wind speed in m/s.
        timestamp_col: Name of the column containing the observation timestamp.

    Returns:
        A list of cleaned record dictionaries with keys 'turbine_id',
        'timestamp', 'wind_speed', and 'power'.
    """
    raw_rows = parse_csv(filepath)
    records = []
    for row in raw_rows:
        record = {
            "turbine_id": row.get(turbine_id_col, ""),
            "timestamp": normalize_timestamp(row.get(timestamp_col, "")),
            "wind_speed": clean_numeric(row.get(wind_speed_col, "")),
            "power": clean_numeric(row.get(power_col, "")),
        }
        records.append(record)
    return records
