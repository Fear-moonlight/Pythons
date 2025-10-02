# -*- coding: utf-8 -*-
import os
import pandas as pd

# Path to your directory with Excel files
input_directory = "./input"
output_file = "combined_output.csv"

col_indices = [0, 1, 2, 3, 4, 7, 13, 14, 15, 16, 19, 22]

all_data = []

for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(input_directory, filename)
        try:
            df_full = pd.read_excel(filepath, sheet_name="RSL", engine="openpyxl", header=None)
            df_selected = df_full.iloc[:, col_indices].copy()

            # Remove rows that contain header-like strings (e.g. "Actual", "Rx", etc.)
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and any(w in x.lower() for w in ["actual", "rx", "tx", "power"])
                ).any(axis=1)
            ]

            # Remove rows with "Automation Needed" or "AFTER MIGRATION"
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and x.strip().lower() in ["automation needed", "after migration"]
                ).any(axis=1)
            ]

            # Drop rows where all selected columns are empty
            df_selected.dropna(how='all', inplace=True)

            all_data.append(df_selected)

        except Exception as e:
            print(f"❌ Failed to read {filename}: {e}")

# Save the combined result to CSV
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False, header=False)
    print(f"✅ Final cleaned data saved to: {output_file}")
else:
    print("⚠️ No valid data found.")