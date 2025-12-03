#!/usr/bin/env python3

from modulefinder import test
import sys
from tracemalloc import start

def clean_data(filename):
    """Read the single-line input and split into range strings."""
    with open(filename, "r") as f:
        data = f.read().strip()
    # Split on commas and drop any empty segments (e.g. from trailing comma)
    print([segment for segment in data.split(",") if segment])
    return [segment for segment in data.split(",") if segment]

def is_invalid_id(id):
    """
    An ID is invalid if its decimal representation is composed of some
    non-empty sequence of digits repeated exactly twice.

    Examples:
      55      -> "5" repeated twice
      6464    -> "64" repeated twice
      123123  -> "123" repeated twice
    """
    
    if len(str(id)) % 2 != 0:
        return False
    else:
        midpoint = len(id) // 2
        firstpart = id[:midpoint]
        secondpart = id[midpoint:]
        return True if firstpart == secondpart else False

def calculate_invalid_id_sum(ranges):
    invalid_id_sum = 0

    for range_string in ranges:
        start_str, end_str = range_string.split("-")
        start_int = int(start_str)
        end_int = int(end_str)

        for test_id in range(start_int, end_int):
            print("ID: ", test_id)
            invalid_id_sum += test_id if is_invalid_id(str(test_id)) else 0
        
    return invalid_id_sum

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "day2.txt"
    ranges = clean_data(filename)
    answer = calculate_invalid_id_sum(ranges)
    print("Final answer:", answer)

if __name__ == "__main__":
    main()