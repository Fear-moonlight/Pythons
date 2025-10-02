import os
import pandas as pd

# Set input folder and output file
input_directory = "./input"  # ⬅️ Replace with your path
output_file = "l3vpn_ac_output.csv"

col_map = {
    3: "D",
    5: "F",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",       # → used in Result_P
    18: "S",
    19: "T",
    28: "AC",
    29: "AD",
    30: "AE",
    31: "AF",
    32: "AG"       # → used in Result_AG
}

col_indices = list(col_map.keys())

all_data = []

for filename in os.listdir(input_directory):
    if filename.endswith(".xlsx") and not filename.startswith("~$"):
        filepath = os.path.join(input_directory, filename)
        try:
            df = pd.read_excel(filepath, sheet_name="L3VPN AC", engine="openpyxl", header=None)
            df_selected = df.iloc[:, col_indices].copy()
            df_selected.columns = list(col_map.values())  # rename columns to labels

            # Remove header-like rows
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and any(w in x.lower() for w in ["actual", "rx", "tx", "power"])
                ).any(axis=1)
            ]

            # Remove rows containing 'Sub-int'
            df_selected = df_selected[
                ~df_selected.applymap(
                    lambda x: isinstance(x, str) and "sub-int" in x.lower()
                ).any(axis=1)
            ]

            # Drop fully empty rows
            df_selected.dropna(how="all", inplace=True)

            # Compute Result_P and Result_AG
            df_selected["Result_P"] = df_selected["P"].apply(
                lambda x: "Pass" if str(x).strip() == "0%" else ("Fail" if str(x).strip() == "100%" else "")
            )
            df_selected["Result_AG"] = df_selected["AG"].apply(
                lambda x: "Pass" if str(x).strip() == "0%" else ("Fail" if str(x).strip() == "100%" else "")
            )

            all_data.append(df_selected)

        except Exception as e:
            print(f"❌ Failed to read {filename}: {e}")

# Combine and save
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False, header=False)
    print(f"✅ Data with Pass/Fail saved to: {output_file}")
else:
    print("⚠️ No valid data found.")