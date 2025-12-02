#!/usr/bin/env python3

import sys

def clean_data(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    # make data into list of tuples, where each tuple is (direction, value)
    data = [(line[0], int(line[1:])) for line in data]
    return data

def calculate_password(filename):
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

    for direction, value in rotations:
        instructions_executed += 1
        print(f"--- Executing instruction #{instructions_executed} ---")
        print("Current Dial Position:", dial_position)
        print("Direction:", direction, " Value:", value)

        if direction == 'R':
            dial_position += value
        elif direction == 'L':
            dial_position -= value
        
        dial_position %= 100
        print("New Dial Position:", dial_position)

        if dial_position == 0:
            password += 1
            print("Dial hit 0! Incrementing password to:", password)

    return password

def main():
    print("Calculating...")
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    answer = calculate_password(filename)
    print(answer)
    return answer

if __name__ == "__main__":
    main()