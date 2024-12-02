import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Open the file
with open(input_path, 'r') as file:
    lines = file.readlines()

safe_count = 0  # Counter for safe reports

for line in lines:
    values = list(map(int, line.strip().split()))  # Convert row to a list of integers
    is_increasing = True
    is_decreasing = True

    for i in range(len(values) - 1):
        diff = values[i+1] - values[i]

        if not (1 <= abs(diff) <= 3):  # Check the difference rule
            is_increasing = is_decreasing = False
            break

        if diff > 0:  # Increasing trend
            is_decreasing = False
        elif diff < 0:  # Decreasing trend
            is_increasing = False

    # A report is safe if it's either fully increasing or fully decreasing
    if is_increasing or is_decreasing:
        safe_count += 1

# Print the result
print(f"The total number of safe reports is: {safe_count}")