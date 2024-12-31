import math
from itertools import combinations

def parse_map(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.isalnum():  # Valid frequency
                antennas.setdefault(cell, []).append((x, y))
    return antennas

def is_collinear(p1, p2, p3):
    # Tolerance float to help avoid precision error when rounding.
    TOLERANCE = 0.00000000001
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < TOLERANCE

def find_antinodes_part2(grid):
    antennas = parse_map(grid)
    antinodes = set()
    width, height = len(grid[0]), len(grid)

    # For each frequency, find all points that are collinear with at least two antennas
    for freq, positions in antennas.items():
        # Check all points in the grid
        for y in range(height):
            for x in range(width):
                point = (x, y)
                collinear_count = 0

                # Count how many antennas are collinear with this point
                for p1, p2 in combinations(positions, 2):
                    if is_collinear(p1, point, p2):
                        collinear_count += 1
                        break  # Once we confirm collinearity with two antennas, we can stop

                # If at least two antennas are collinear with this point, it's an antinode
                if collinear_count > 0:
                    antinodes.add(point)

    return antinodes

def generate_map_with_antinodes(grid, antinodes):
    grid_map = [list(row) for row in grid]

    for x, y in antinodes:
        if 0 <= x < len(grid_map[0]) and 0 <= y < len(grid_map):
            if grid_map[y][x] == '.': 
                grid_map[y][x] = '#'

    return [''.join(row) for row in grid_map]

def print_map(grid):
    for row in grid:
        print(row)

def solve_puzzle(input_file, part=1):
    with open(input_file, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    if part == 2:
        antinodes = find_antinodes_part2(grid)
    else:
        raise ValueError("This function is only for Part 2.")

    updated_grid = generate_map_with_antinodes(grid, antinodes)
    print(f"\nFinal map with antinodes (#) for Part {part}:")
    print_map(updated_grid)

    return len(antinodes)

if __name__ == "__main__":
    try:
        result = solve_puzzle("2024/08/input.txt", part=2)
        print(f"\nPuzzle answer Part 2: {result}")
    except FileNotFoundError:
        print("Input File not found")
