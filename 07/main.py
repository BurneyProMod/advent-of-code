import os
from itertools import product

def read_input_file(file_name='input.txt'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, file_name)
    with open(input_path, 'r') as file:
        content = file.read()
    return content

# Puts the input from file into Tuples.
# Tuple = {Target Value, List of Numbers}
def parse_input(data):
    equations = []
    for line in data.strip().split('\n'):
        target, numbers = line.split(':')
        target = int(target.strip())
        numbers = list(map(int, numbers.split()))
        equations.append((target, numbers))
    return equations


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

# Finds all equations where some combinations of operators produce the target value, then adds them into var total
def find_valid_equations(equations):
    total = 0
    for target, numbers in equations:
        num_operators = len(numbers) - 1
        valid = False
        
        # Generate all possible combinations of operators
        for operators in product(['+', '*', '||'], repeat=num_operators):
            if evaluate_expression(numbers, operators) == target:
                valid = True
                break
        
        if valid:
            total += target
    return total

if __name__ == "__main__":
    input_data = read_input_file('input.txt')
    
    equations = parse_input(input_data)
    
    result = find_valid_equations(equations)
    
    print("Total:", result)
