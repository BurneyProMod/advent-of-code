import os

def calcArea(length, width, height):
    area = 2*length*width + 2*width*height + 2*height*length
    return area

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Get each line from the input file
with open(input_path, 'r') as file:
    # Read all lines and strip newlines
    presents = [line.strip() for line in file.readlines()]

# Part 1
totalPaper = 0
for present in presents:
    length, width, height = present.split('x')
    length = int(length)
    width = int(width)
    height = int(height)
    area = calcArea(length, width, height)
    smallestSide = min(length*width, width*height, height*length)
    totalPaper += area + smallestSide
print ("Total paper needed: ", totalPaper)

# Part 2
totalRibbon = 0
for present in presents:
    length, width, height = present.split('x')
    length = int(length)
    width = int(width)
    height = int(height)
    perimeter = 2*min(length+width, width+height, height+length)
    volume = length * width * height
    totalRibbon += perimeter + volume
print ("Total ribbon needed: ", totalRibbon)