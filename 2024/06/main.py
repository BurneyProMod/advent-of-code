import os
import time
import sys

def parse_map(file_path):
    with open(file_path, 'r') as f:
        return [list(row) for row in f.read().split('\n') if row.strip()]

def find_guard_start(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return x, y, 0  # x, y, direction (0: up, 1: right, 2: down, 3: left)
    return None

def move_guard(grid, x, y, direction):
    dx_dy = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Directions: 0 = up, 1 = right, 2 = down, 3 = left
    next_x = x + dx_dy[direction][0]
    next_y = y + dx_dy[direction][1]

    if (next_x < 0 or next_x >= len(grid[0]) or
        next_y < 0 or next_y >= len(grid) or
        grid[next_y][next_x] == '#'):
        # Turn right if blocked
        return x, y, (direction + 1) % 4

    # Move forward
    return next_x, next_y, direction

def trace_guard_path(grid, x, y, direction):
    visited_positions = []
    states = set()
    steps = 0

    while steps < 10000:  # Limit to avoid infinite loops
        state = (x, y, direction)
        if state in states:
            break  # Loop detected
        states.add(state)
        visited_positions.append((x, y))

        x, y, direction = move_guard(grid, x, y, direction)
        steps += 1

        # Stop if the guard leaves the grid
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            break

    return visited_positions

def simulate_with_obstacle(grid, x, y, direction, obstacle):
    visited_states = set()
    steps = 0
    ox, oy = obstacle

    while steps < 10000:
        # Check obstacle interaction
        if (x, y) == (ox, oy):
            return False  # Hit the obstacle, not a loop
        
        state = (x, y, direction)
        if state in visited_states:
            return True  # Loop detected
        
        visited_states.add(state)
        x, y, direction = move_guard(grid, x, y, direction)
        steps += 1

        # Out of bounds means no loop
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return False

    return False  # No loop detected

def visualize_progress(current, total, testing_obstacle, loops_found):
    sys.stdout.write("\033c")  # Clear the terminal
    print(f"\n{'=' * 40}")
    print(f"Guard Loop Simulation\n{'=' * 40}")
    print(f"Testing Obstacle: {testing_obstacle}")
    print(f"Progress: {current}/{total} ({current / total:.2%})")
    print(f"Loops Found: {loops_found}")
    print(f"{'=' * 40}\n")
    sys.stdout.flush()

def solve_part_two(file_path):
    grid = parse_map(file_path)
    start_position = find_guard_start(grid)
    if start_position is None:
        raise ValueError("Guard's starting position not found in the grid.")
    
    x, y, direction = start_position

    # Trace the guard's original path
    guard_path = trace_guard_path(grid, x, y, direction)

    # Test placing obstacles only along the guard's original path
    loop_positions = 0
    total_positions = len(guard_path)

    for idx, obstacle in enumerate(guard_path):
        if grid[obstacle[1]][obstacle[0]] == '#':
            continue  # Skip walls

        visualize_progress(idx + 1, total_positions, obstacle, loop_positions)

        if simulate_with_obstacle(grid, x, y, direction, obstacle):
            loop_positions += 1
            
        time.sleep(0.01)  # Optional: slows down updates for readability

    visualize_progress(total_positions, total_positions, None, loop_positions)
    return loop_positions

# Run the optimized solution with visualization
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
part_two_result = solve_part_two(file_path)
print(f"Part Two Result: {part_two_result}")
