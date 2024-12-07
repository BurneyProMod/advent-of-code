from collections import defaultdict, deque
import os

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]  # Ensure lines are strings

    # Split into rules and updates
    rules_section = []
    updates_section = []
    is_updates = False

    for line in lines:
        if not line:  # Empty line separates sections
            is_updates = True
            continue
        if is_updates:
            updates_section.append(line.strip())
        else:
            rules_section.append(line.strip())

    # Parse rules
    rules = []
    for rule in rules_section:
        x, y = map(int, rule.split("|"))
        rules.append((x, y))

    # Parse updates
    updates = [list(map(int, update.split(","))) for update in updates_section]

    return rules, updates

def is_update_valid(update, rules):
    """Check if an update satisfies all applicable rules."""
    for x, y in rules:
        if x in update and y in update:
            # Ensure x appears before y in the update
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_number(update):
    """Find the middle number of an update."""
    return update[len(update) // 2]

def topological_sort(nodes, edges):
    """Perform a topological sort to reorder pages based on the rules."""
    # Create adjacency list and in-degree counter
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in edges:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x]  # Ensure every node is in the in-degree dictionary

    # Queue of nodes with no incoming edges
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_nodes = []

    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_nodes

def reorder_update(update, rules):
    """Reorder an update based on the rules using topological sort."""
    # Use only the nodes and edges relevant to this update
    nodes = set(update)
    edges = [(x, y) for x, y in rules if x in nodes and y in nodes]
    sorted_nodes = topological_sort(nodes, edges)

    # Return the sorted nodes in the order they appear in the update
    return [node for node in sorted_nodes if node in update]

def calculate_reordered_updates(file_path):
    """Calculate the sum of middle page numbers of reordered incorrect updates."""
    rules, updates = parse_input(file_path)
    total_sum = 0

    for update in updates:
        if not is_update_valid(update, rules):  # Find incorrect updates
            reordered_update = reorder_update(update, rules)  # Reorder the update
            total_sum += find_middle_number(reordered_update)  # Add the middle page number

    return total_sum


# Define the input file path
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input.txt')

# Calculate the result
result = calculate_reordered_updates(input_path)
print(f"The sum of the middle page numbers from reordered incorrect updates is: {result}")
