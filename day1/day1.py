#!/usr/bin/env python3


def calculate_password(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    print(lines)
    password = 0
    return password

def main():
    print("Calculating...")
    answer = calculate_password("input.txt")
    print(answer)
    return 0