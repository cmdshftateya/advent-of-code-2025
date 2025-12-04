#!/usr/bin/env python3

import sys

def clean_data(filename):
    """Open and clean"""
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
    return lines

def get_bank_joltage(bank):
    """
    The joltage calculation is finding the largest 12-digit number you can make
    by turning on exactly twelve batteries, keeping their left-to-right order
    (i.e., choosing a length-12 subsequence of digits).
    """
    bank = bank.strip()
    target_len = 12

    joltage = ""
    search_start = 0

    # Greedy: for each digit position, pick the best digit we can while still
    # leaving enough digits to fill out the remaining positions.
    while len(joltage) < target_len:
        remaining = target_len - len(joltage)
        # Last index we can START from so that there are `remaining` digits left.
        # +1 because slice end is exclusive.
        search_end = len(bank) - remaining + 1

        options = bank[search_start:search_end]
        next_digit = max(options)

        # First occurrence of that best digit within our current options window.
        next_digit_index = search_start + options.index(next_digit)

        joltage += next_digit
        search_start = next_digit_index + 1  # move past the chosen digit

    return int(joltage)

def get_total_joltage(input):
    banks = clean_data(input)
    total_output_joltage = 0
    for bank in banks:
        total_output_joltage += get_bank_joltage(bank)
    return total_output_joltage

def main():
    print("Total output joltage: ", get_total_joltage("day3.txt"))

if __name__ == "__main__":
    main()