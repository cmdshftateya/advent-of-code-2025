#!/usr/bin/env python3

import sys

def txt_to_wall(filename):
    """Read the grid from file and return as 2D list."""
    wall = []
    with open(filename, "r") as f:
        for line in f:
            row = list(line.strip())
            wall.append(row)
    return wall

def check_surrounding(wall, row, col):
    """
    Check the 8 surrounding cells to count how many contain '@'.
    Returns 1 if fewer than 4 adjacent '@' symbols (accessible), 0 otherwise.
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    adjacent_count = 0
    for dr, dc in directions:
        neighbor_row = row + dr
        neighbor_col = col + dc
        # Check bounds and count adjacent '@' symbols
        if 0 <= neighbor_row < len(wall) and 0 <= neighbor_col < len(wall[0]):
            if wall[neighbor_row][neighbor_col] == "@":
                adjacent_count += 1
    
    # Accessible if fewer than 4 adjacent rolls
    return 1 if adjacent_count < 4 else 0

def count_rolls(wall, remove=False):
    """
    Count rolls of paper that can be accessed (fewer than 4 adjacent '@' symbols).
    If remove=True, marks accessible rolls as '.' (removed) in the wall.
    Returns the count of accessible rolls.
    """
    accessible_count = 0
    to_remove = []
    
    # First pass: identify all accessible rolls
    for row in range(len(wall)):
        for col in range(len(wall[0])):
            if wall[row][col] == "@":
                if check_surrounding(wall, row, col) == 1:
                    accessible_count += 1
                    to_remove.append((row, col))
    
    # Second pass: remove the accessible rolls if requested
    if remove:
        for row, col in to_remove:
            wall[row][col] = "."
    
    return accessible_count

def count_rolls_part2(wall):
    """
    Iteratively remove accessible rolls until no more can be removed.
    Returns total count of removed rolls.
    """
    total_removed = 0
    
    # Keep removing accessible rolls until no more can be removed
    while True:
        # Find all currently accessible rolls
        accessible_positions = []
        for row in range(len(wall)):
            for col in range(len(wall[0])):
                if wall[row][col] == "@":
                    if check_surrounding(wall, row, col) == 1:
                        accessible_positions.append((row, col))
        
        # If no accessible rolls, we're done
        if len(accessible_positions) == 0:
            break
        
        # Remove all accessible rolls
        for row, col in accessible_positions:
            wall[row][col] = "."
        
        total_removed += len(accessible_positions)
    
    return total_removed

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "day04.txt"
    part = sys.argv[2] if len(sys.argv) > 2 else "1"
    
    wall = txt_to_wall(filename)
    
    # Print initial state
    for row in wall:
        print("".join(row))
    print()
    
    if part == "1":
        result = count_rolls(wall, remove=False)
        print(result)
    elif part == "2":
        result = count_rolls_part2(wall)
        print(result)
    else:
        print("Invalid part")

if __name__ == "__main__":
    main()