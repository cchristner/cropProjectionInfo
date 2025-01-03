import pandas as pd
import re

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False, border=1, classes='dataframe')

# Open the original HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Replace the existing table with the new HTML table
updated_html_content = re.sub(
    r'<table.*?>.*?</table>',
    html_table,
    html_content,
    flags=re.DOTALL
)

# Save the updated HTML content back to the file
with open('index.html', 'w') as file:
    file.write(updated_html_content)
