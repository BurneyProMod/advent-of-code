import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Open the file
with open(input_path, 'r') as file:
    lines = file.readlines()

def is_safe(values):
    is_increasing = all(1 <= values[i+1] - values[i] <= 3 for i in range(len(values) - 1))
    is_decreasing = all(-3 <= values[i+1] - values[i] <= -1 for i in range(len(values) - 1))
    return is_increasing or is_decreasing

def is_safe_with_dampener(values):
    for i in range(len(values)):
        modified_values = values[:i] + values[i+1:]  # Remove the current level
        if is_safe(modified_values):
            return True
    return False

safe_count = 0

for line in lines:
    values = list(map(int, line.strip().split()))
    if is_safe(values) or is_safe_with_dampener(values):
        safe_count += 1

print(f"The total number of safe reports is: {safe_count}")
