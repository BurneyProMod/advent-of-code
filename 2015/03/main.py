import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Get each line from the input file
with open(input_path, 'r') as file:
    # Read all lines and strip newlines
    directions = list(file.read().strip())

# Part 1
x, y = 0, 0  # Santa starts at origin
houses = {(0,0)}  # Set of visited houses, starting position

for direction in directions:
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    houses.add((x,y))

print("Houses visited:", len(houses))

# Part 2
class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.houses = {(0,0)}

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '>':
            self.x += 1
        elif direction == '<':
            self.x -= 1
        self.houses.add((self.x, self.y))

humanSanta = Santa()
robotSanta = Santa()

for i, direction in enumerate(directions):
    if i % 2 == 0:
        humanSanta.move(direction)
    else:
        robotSanta.move(direction)

print("Human Santa Visited: ", len(humanSanta.houses))
print("Robot Santa Visited: ", len(robotSanta.houses))
print("Total Houses Visited: ", len(humanSanta.houses.union(robotSanta.houses)))