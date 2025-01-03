import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Convert the DataFrame to an HTML table
html_table = df.to_html(index=False, border=1, classes='dataframe')

# Open the original HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Replace the placeholder with the generated HTML table
updated_html_content = html_content.replace(
    "<!-- Paste the generated HTML table here -->",
    html_table
)

# Save the updated HTML content back to the file
with open('index.html', 'w') as file:
    file.write(updated_html_content)
