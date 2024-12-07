import os

def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    pattern = "MAS"
    reverse_pattern = pattern[::-1]
    count = 0

    def is_valid(x, y):
        """Check if (x, y) is within the grid."""
        return 0 <= x < rows and 0 <= y < cols

    def is_xmas(x, y):
        """Check if the cell at (x, y) is the center of an X-MAS."""
        # Check the top-left to bottom-right diagonal
        if not all(
            is_valid(x + dx, y + dx)
            for dx in range(-1, 2)
        ) or not all(
            is_valid(x - dx, y + dx)
            for dx in range(-1, 2)
        ):
            return False

        # Get the diagonal strings
        tl_br = ''.join(grid[x + dx][y + dx] for dx in range(-1, 2))  # Top-left to bottom-right
        bl_tr = ''.join(grid[x - dx][y + dx] for dx in range(-1, 2))  # Bottom-left to top-right

        # Check if both diagonals form MAS or SAM
        return (
            (tl_br == pattern or tl_br == reverse_pattern) and
            (bl_tr == pattern or bl_tr == reverse_pattern)
        )

    # Traverse the grid
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_xmas(r, c):
                count += 1

    return count


# Read the grid from input.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

with open(input_path, 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

# Count occurrences
result = count_xmas_occurrences(grid)
print(f"The number of X-MAS patterns is: {result}")