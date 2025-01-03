import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False)

# Save the HTML table to a file
with open('table.html', 'w') as f:
    f.write(html_table)
