import os
import re

def extract_table_from_readme(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Match the table starting with "| Day" and ending before the next blank line
    match = re.search(r"(\| Day\s+\|.*?)(\n\n|$)", content, re.DOTALL)
    if match:
        return match.group(1)  # Return the matched table
    return None

# Adds year to table if there is a directory for that year in the repository
def get_year_directories():
    current_dir = os.getcwd()
    year_dirs = []

    for entry in os.listdir(current_dir):
        if entry.isdigit() and os.path.isdir(entry):
            readme_path = os.path.join(entry, "README.md")
            if os.path.isfile(readme_path): # Does not add the year if there is no README.md file
                year_dirs.append(entry)

    # Sort years numerically
    return sorted(year_dirs)

def update_parent_readme(years):
    parent_readme_path = "README.md"
    parent_content = [
        "# 🌟 Advent of Code Star Tracker 🎄✨",
        "",
        "[Advent of Code](https://adventofcode.com/)",
        "",
        "## 📅 Yearly Progress",
        ""
    ]

    for year in years:
        year_readme_path = f"{year}/README.md"
        if os.path.exists(year_readme_path):
            table = extract_table_from_readme(year_readme_path)
            if table:
                parent_content.append(f"### {year}\n")
                parent_content.append(table)
                parent_content.append("")

    # Write the updated parent README.md
    with open(parent_readme_path, "w") as file:
        file.write("\n".join(parent_content))

if __name__ == "__main__":
    years = get_year_directories()
    update_parent_readme(years)