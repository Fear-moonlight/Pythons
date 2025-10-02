import pandas as pd

# Load the two CSVs
bgp = pd.read_csv("/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/Parse_BGP_to_excel/bgp.csv")
bgp1 = pd.read_csv("/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/Parse_BGP_to_excel/bgp1.csv")

# Ensure consistent column names (assuming 4 columns: A, B, C, D)
# Adjust names if they are already labeled
bgp.columns = ["A", "B", "C", "D"]
bgp1.columns = ["A", "B", "C", "D"]

# Merge on column A (Network), keeping only duplicates
merged = pd.merge(bgp[["A", "D"]], bgp1[["A", "D"]], on="A", how="inner", suffixes=("_bgp", "_bgp1"))

# Rename columns for clarity
merged = merged.rename(columns={"A": "Network", "D_bgp": "bgp_AS_Path", "D_bgp1": "bgp1_AS_Path"})
merged = merged.drop_duplicates()
# Save to CSV
merged.to_csv("duplicates.csv", index=False)

print("✅ Done! Results saved to duplicates.csv")