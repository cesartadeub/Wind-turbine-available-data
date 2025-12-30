#!/usr/bin/env python3
"""
parse_data.py - Parse wind turbine data files.

This script reads CSV files containing wind turbine performance data
and extracts relevant columns for analysis.
"""

import csv
import sys

def parse_csv(file_path):
    """Parse a CSV file and return a list of dictionaries."""
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_data.py <csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    data = parse_csv(file_path)
    print(f"Parsed {len(data)} rows.")
    # TODO: Add more processing steps

if __name__ == "__main__":
    main()