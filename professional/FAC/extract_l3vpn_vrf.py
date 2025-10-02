import os
import pandas as pd

input_directory = "./input"  # ⬅️ Replace with your path
output_file = "l3vpn_vrf_output.csv"

# Columns to extract: B=1, C=2, E=4, F=5
col_indices = [1, 2, 4, 5]

all_data = []


for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(input_directory, filename)
        try:
            df = pd.read_excel(filepath, sheet_name="L3VPN VRF", engine="openpyxl", header=None)
            df_selected = df.iloc[:, col_indices].copy()

            # Remove rows with header-like text
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and any(w in x.lower() for w in ["actual", "rx", "tx", "power"])
                ).any(axis=1)
            ]

            # Remove rows containing "VPN-Instance"
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and "vpn-instance" in x.lower()
                ).any(axis=1)
            ]

            # Drop rows where all selected values are empty
            df_selected.dropna(how="all", inplace=True)

            all_data.append(df_selected)

        except Exception as e:
            print(f"❌ Failed to read {filename}: {e}")

if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.drop_duplicates(subset=combined_df.columns[0], inplace=True)  # Remove duplicates based on first column
    combined_df.to_csv(output_file, index=False, header=False)
    print(f"✅ Data extracted, duplicates removed, saved to: {output_file}")
else:
    print("⚠️ No valid data found in the files.")