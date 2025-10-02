import os
import pandas as pd

# Folder path with Excel files
input_directory = "./input"  # ⬅️ Replace with your actual folder
output_file = "eline_output.csv"

# Columns to extract from Eline sheet (0-indexed)
col_indices = [2 ,3, 7, 8, 9, 11, 17]

# Collect all cleaned data
all_eline_data = []

for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(input_directory, filename)
        try:
            # Read the ELINE sheet with no headers
            df_full = pd.read_excel(filepath, sheet_name="ELINE", engine="openpyxl", header=None)

            # Extract the selected columns and make a copy
            df_selected = df_full.iloc[:, col_indices].copy()

            # Drop rows with any blank cell
            df_selected.dropna(how='any', inplace=True)

            # Drop rows containing "Sub-int" in any cell (case-insensitive)
            df_selected = df_selected[~df_selected.applymap(
                lambda x: isinstance(x, str) and x.strip().lower() == "sub-int"
            ).any(axis=1)]

            # Drop rows with headers like "actual", "rx", "tx", "power"
            df_selected = df_selected[~df_selected.applymap(
                lambda x: isinstance(x, str) and any(word in x.lower() for word in ["actual", "rx", "tx", "power"])
            ).any(axis=1)]

            all_eline_data.append(df_selected)

        except Exception as e:
            print(f"❌ Failed to process '{filename}': {e}")

# Save to CSV (no headers)
if all_eline_data:
    combined_df = pd.concat(all_eline_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False, header=False)
    print(f"✅ Clean ELINE data saved to: {output_file}")
else:
    print("⚠️ No valid ELINE data found.")