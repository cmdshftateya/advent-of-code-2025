#!/usr/bin/env python3

import sys

def clean_data(filename):
    """Parse rotation instructions from file.
    
    Right rotation adds value, left rotation subtracts value.
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    
    rotations = []
    for line in lines:
        direction, value = line[0], int(line[1:])
        rotation = value if direction == 'R' else -value
        rotations.append(rotation)
    
    return rotations

def calculate_password_part1(filename):
    rotations = clean_data(filename)

    # Rotations to the right increase the password by the value,
    # rotations to the left decrease the password by the value.
    
    # The dial starts by pointing at 50.

    # Because the dial is a circle, 
    #     turning the dial left from 0 one click makes it point at 99. 
    #     Similarly, turning the dial right from 99 one click makes it point at 0.
    
    # So if the dial crosses 99, we should reset it to 0
    # And if the dial crosses 0, we should reset it to 99
    # Every time the dial is set to 0, we should increment the password by 1.

    dial_position = 50
    instructions_executed = 0

    #Now calculate the password
    password = 0

    for rotation in rotations:
        instructions_executed += 1
        print(f"--- Executing instruction #{instructions_executed} ---")
        print("Current Dial Position:", dial_position)
        
        # rotation is positive for R, negative for L
        direction = 'R' if rotation > 0 else 'L'
        value = abs(rotation)
        print("Direction:", direction, " Value:", value)

        dial_position = (dial_position + rotation) % 100
        print("New Dial Position:", dial_position)

        if dial_position == 0:
            password += 1
            print("Dial hit 0! Incrementing password to:", password)

    return password

def calculate_password_part2(filename):
    """Part 2: Count how many times the dial points at 0 during any rotation."""
    rotations = clean_data(filename)

    dial = 50
    password = 0

    for r in rotations:
        step = 1 if r > 0 else -1
        for _ in range(abs(r)):
            dial = (dial + step) % 100
            if dial == 0:
                password += 1

    return password


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "day1input.txt"
    
    print("Part 1: Counting zeros after each rotation...")
    answer1 = calculate_password_part1(filename)
    print(f"Part 1 answer: {answer1}")
    
    print("\nPart 2: Counting zeros during rotations...")
    answer2 = calculate_password_part2(filename)
    print(f"Part 2 answer: {answer2}")
    
    return answer1, answer2

if __name__ == "__main__":
    main()