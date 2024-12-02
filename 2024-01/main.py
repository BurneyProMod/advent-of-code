# https://adventofcode.com/2024/day/1
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Open the file
with open(input_path, 'r') as file:
    lines = file.readlines()


list1 = []
list2 = []

for line in lines:
    values = line.strip().split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

# Sort lists
list1.sort()
list2.sort()

total = 0
for a, b in zip(list1, list2):
    total += abs(a - b)

# Print result:
print(f"Total distance: {total}")