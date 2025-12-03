#!/usr/bin/env python3

from modulefinder import test
from re import search
import sys
from tracemalloc import start

def clean_data(filename):
    """Read the single-line input and split into range strings."""
    with open(filename, "r") as f:
        data = f.read().strip()
    # Split on commas and drop any empty segments (e.g. from trailing comma)
    return [segment for segment in data.split(",") if segment]

def is_invalid_id(id):
    """
    Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
    So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
    """
    # if it is repeating, we should able to find the original string in the string doubled without looking at the first character
    id = str(id)
    doublestring = id * 2
    searchstring = doublestring[1:-1]
    return True if id in searchstring else False


def calculate_invalid_id_sum(ranges):
    invalid_id_sum = 0

    for range_string in ranges:
        start_str, end_str = range_string.split("-")
        start_int = int(start_str)
        end_int = int(end_str)

        for test_id in range(start_int, end_int):
            invalid_id_sum += test_id if is_invalid_id(str(test_id)) else 0
        
    return invalid_id_sum

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "day2.txt"
    ranges = clean_data(filename)
    answer = calculate_invalid_id_sum(ranges)
    print("Final answer:", answer)

if __name__ == "__main__":
    main()