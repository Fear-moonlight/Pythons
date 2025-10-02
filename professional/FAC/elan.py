import os
import pandas as pd

# Input folder and output file
input_directory = "./input"  # ⬅️ Update path if needed
output_file = "elan_output.csv"

# Column indices: D, E, G, H, I, K, O
col_indices = [3, 4, 6, 7, 8, 10, 14]

all_data = []

for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(input_directory, filename)
        try:
            df_full = pd.read_excel(filepath, sheet_name="ELAN", engine="openpyxl", header=None)
            df_selected = df_full.iloc[:, col_indices].copy()

            # Remove rows with headers like "Actual", "Rx", etc.
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

            # Drop fully empty rows
            df_selected.dropna(how='all', inplace=True)

            all_data.append(df_selected)

        except Exception as e:
            print(f"❌ Failed to read {filename}: {e}")

# Save result to CSV
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False, header=False)
    print(f"✅ Cleaned ELAN data saved to: {output_file}")
else:
    print("⚠️ No valid data found.")
