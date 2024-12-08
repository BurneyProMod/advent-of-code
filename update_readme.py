import os
import re

# Extract star tracker table from {year}/README.md
def extract_yearly_table(year_readme_path):
    with open(year_readme_path, "r") as file:
        content = file.read()
    match = re.search(r"\| Day.*?\|\n(\|.*?\n)+", content, re.DOTALL)
    return match.group(0) if match else ""

# Update 
def update_parent_readme(parent_readme_path, yearly_tables):
    with open(parent_readme_path, "w") as file:
        # Write header
        file.write("# 🌟 Advent of Code Star Tracker 🎄✨\n\n")
        file.write("[Advent of Code](https://adventofcode.com/)\n\n")
        file.write("## 📅 Yearly Progress\n\n")

        # Add tables
        for year, table in yearly_tables.items():
            file.write(f"### {year}\n\n")
            file.write(table + "\n\n")

def main():
    root_dir = os.getcwd()
    parent_readme_path = os.path.join(root_dir, "README.md")

    # Find all yearly README.md files
    yearly_tables = {}
    for year_dir in sorted(os.listdir(root_dir)):
        year_path = os.path.join(root_dir, year_dir)
        if os.path.isdir(year_path) and year_dir.isdigit():
            year_readme_path = os.path.join(year_path, "README.md")
            if os.path.exists(year_readme_path):
                table = extract_yearly_table(year_readme_path)
                if table:
                    yearly_tables[year_dir] = table

    # Update root README
    update_parent_readme(parent_readme_path, yearly_tables)

if __name__ == "__main__":
    main()