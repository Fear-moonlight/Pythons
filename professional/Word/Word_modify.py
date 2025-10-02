import pandas as pd
from docx import Document

# Load the Excel file
df = pd.read_excel('variables.xlsx', sheet_name='Sheet1')

# Convert the DataFrame to a dictionary
replacements = pd.Series(df.Value.values, index=df.Placeholder).to_dict()

# Load the Word document
doc = Document('Test.docx')

# Function to replace text in paragraphs
def replace_text_in_paragraph(paragraph, replacements):
    for key, value in replacements.items():
        if key in paragraph.text:
            inline = paragraph.runs
            for item in inline:
                if key in item.text:
                    item.text = item.text.replace(key, value)

# Replace text in paragraphs
for paragraph in doc.paragraphs:
    replace_text_in_paragraph(paragraph, replacements)

# Save the modified document
doc.save('modified_example.docx')