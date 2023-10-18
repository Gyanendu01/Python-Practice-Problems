# Define the number of rows you want in the table
num_rows = 5

# Create the table header
header = "| Number | Square | Cube |\n|--------|--------|------|"

# Initialize an empty string to store the table rows
table_rows = ""

# Generate the table rows for numbers, squares, and cubes
for num in range(1, num_rows + 1):
    square = num ** 2
    cube = num ** 3
    table_rows += f"| {num} | {square} | {cube} |\n"

# Combine the header and table rows
table = f"{header}\n{table_rows}"

# Print the table in Markdown format
print(table)
