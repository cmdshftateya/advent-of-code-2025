#!/usr/bin/env python3

import sys

def clean_data(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data.split(",")

def calculate_invalid_id_sum(data):
    invalid_id_sum = 0

    # hardcode for now
    data = ["25-61"]
    for range_string in data:
        start, end = range_string.split("-")
        for i in range(int(start), int(end) + 1):
            print(i)
            # add invalid id to invalid_id_sum
    return invalid_id_sum


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "day2.txt"
    print(function(clean_data(filename)))

if __name__ == "__main__":
    main()