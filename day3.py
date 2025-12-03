#!/usr/bin/env python3

import sys

def clean_data(filename):
    """Open and clean"""
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
    return lines

def get_bank_joltage(bank):
    # find the index of the highest value in the bank unless it is the last value
    max_joltage = max(bank[:-1])
    max_joltage_index = bank.find(max_joltage)
    # now that we know where the max joltage is, we have to find the second highest one *after* the max one
    second_highest_joltage = max(bank[max_joltage_index+1:])
    # print(max_joltage, second_highest_joltage)
    joltage = int(str(max_joltage) + str(second_highest_joltage))
    # print(joltage)
    return joltage

def get_total_joltage(input):
    banks = clean_data(input)
    total_output_joltage = 0
    for bank in banks:
        total_output_joltage += get_bank_joltage(bank)
    return total_output_joltage

def main():
    print(get_total_joltage("day3.txt"))

if __name__ == "__main__":
    main()