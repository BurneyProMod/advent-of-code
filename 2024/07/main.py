import os
import sys
from itertools import product
from time import sleep

# Reads file and returns as string
def read_input_file(file_name='input.txt'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, file_name)
    with open(input_path, 'r') as file:
        content = file.read()
    return content

# Parses input into tuples
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

def format_equation(numbers, operators):
    equation = str(numbers[0])
    for i, operator in enumerate(operators):
        equation += f" {operator} {numbers[i + 1]}"
    return equation

def display_window(equations, current_index, operators_tested, current_result, total_sum, valid_indices, current_fixed_ops):
    sys.stdout.write("\033c")  # Clear the terminal
    print("Evaluating Equations (Real-Time Updates):")
    print(f"{'Idx':<5}{'✔/✖':<5}{'Target':<10}{'Equation':<40}{'Result':<10}")
    print("=" * 70)

    start_index = max(0, current_index - 3)
    end_index = min(len(equations), current_index + 2)  # +1 buffer after current in display

    for i in range(start_index, end_index):
        target, numbers = equations[i]
        status = ""
        formatted_equation = ""
        current_result_display = ""

        if i in valid_indices:
            status = "✔"
            formatted_equation = format_equation(numbers, current_fixed_ops[i])
            current_result_display = target
        elif i < current_index:
            status = "✖"
            formatted_equation = format_equation(numbers, [' '] * (len(numbers) - 1))
        elif i == current_index:
            status = "●"  # Current equation
            formatted_equation = format_equation(numbers, operators_tested)
            current_result_display = current_result

        # Print statement for table lables
        print(
            f"{i + 1:<5}{status:<5}{target:<10}{formatted_equation:<40}{current_result_display:<10}"
        )
    # Print statement for in progress counter
    print("\nTotal Sum:", total_sum)

def find_valid_equations(equations):
    total_sum = 0
    valid_indices = set()
    current_fixed_ops = {}

    for current_index, (target, numbers) in enumerate(equations):
        num_operators = len(numbers) - 1
        result = None

        # Generate all possible combinations of operators
        for operators in product(['+', '*', '||'], repeat=num_operators):
            result = evaluate_expression(numbers, operators)
            display_window(
                equations,
                current_index,
                operators,
                result,
                total_sum,
                valid_indices,
                current_fixed_ops,
            )

            sleep(0.008) # Stops the terminal from flickering.

            if result == target:
                total_sum += target
                valid_indices.add(current_index)
                current_fixed_ops[current_index] = operators
                break

    return total_sum

input_data = read_input_file('input.txt')
equations = parse_input(input_data)
total = find_valid_equations(equations)

print("\nTotal Sum:", total)