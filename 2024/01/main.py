# https://adventofcode.com/2024/day/1
from collections import Counter
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

# Count occurrences in list2
list2_counts = Counter(list2)

# Calculate the similarity score
similarity_score = 0
for number in list1:
    similarity_score += number * list2_counts[number]

# Print the result
print(f"Similarity score: {similarity_score}")
