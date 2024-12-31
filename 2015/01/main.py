import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Get each character from the input file into an array
with open(input_path, 'r') as file:
    # Read the entire file as one string and convert to list of chars
    chars = list(file.read().strip())

# Part 1
currentFloor = 0
for char in chars:
    if char == '(':
        currentFloor += 1
    elif char == ')':
        currentFloor -= 1
print ("Ended at floor: ", currentFloor)

# Part 2
currentFloor = 0
currentPosition = 0
for char in chars:
    if currentFloor != -1:
        currentPosition += 1
        if char == '(':
            currentFloor += 1
        elif char == ')':
            currentFloor -= 1
    else: 
        break
print ("Entered basement at position: ", currentPosition)