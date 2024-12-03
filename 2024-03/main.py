import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

with open(input_path, 'r') as file:
    fileData = file.read()

mulPattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(mulPattern, fileData)

results = []
for x, y in matches:
    results.append(int(x) * int(y))
sumTotal = sum(results)

print(f"The total sum of all valid multiplications is: {sumTotal}")