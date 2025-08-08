import pandas as pd
import re

# List of sheet names to process
sheet_names = ["Low Prod Soil", "Avg Prod Soil", "High Prod Soil"]

# Read the Excel file, specifying the sheet names
dfs = pd.read_excel('data.xlsx', sheet_name=sheet_names, engine='openpyxl')

# Open the original HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Iterate over each sheet and update the HTML content
for sheet_name, df in dfs.items():
    # Replace NaN with empty strings
    df = df.fillna('')

    # Convert the DataFrame to an HTML table
    html_table = df.to_html(index=False, border=1, classes='dataframe')

    # Use regular expressions to find and replace the table for each sheet
    updated_html_content = re.sub(
        rf'<!-- {sheet_name} Table Here -->\s*<table.*?>.*?</table>',
        f'<!-- {sheet_name} Table Here -->\n{html_table}',
        html_content,
        flags=re.DOTALL
    )

    # Update the HTML content for the next iteration
    html_content = updated_html_content

# Save the updated HTML content back to the file
with open('index.html', 'w') as file:
    file.write(updated_html_content)

# print(dfs)