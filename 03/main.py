import os
import re

# Read the input file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

with open(input_path, 'r') as file:
    fileData = file.read()

# Define regex to match instructions
instructionPattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
matches = re.finditer(instructionPattern, fileData)

# At the start of the program, mul instructions are enabled
mulEnabled = True
results = []

# Process each matched instruction
for match in matches:
    if match.group(1) and match.group(2):  # It's a valid `mul(X, Y)`
        if mulEnabled:
            x, y = int(match.group(1)), int(match.group(2))
            results.append(x * y)
    elif match.group(0) == "do()":  # Enable mul instructions
        mulEnabled = True
    elif match.group(0) == "don't()":  # Disable mul instructions
        mulEnabled = False

# Calculate the total sum of all enabled multiplications
sumTotal = sum(results)

# Print the result
print(f"The total sum of all valid enabled multiplications is: {sumTotal}")
