import pandas as pd

# Define the Excel file name
excel_file = 'route_targets_MC_AUP.xlsx'

# Open the Excel file
try:
    xls = pd.ExcelFile(excel_file)
except FileNotFoundError:
    print(f"The file {excel_file} was not found.")
    exit()

# Create an empty list to hold all the data from each sheet
all_data = []

# Iterate over each sheet in the Excel file
for sheet_name in xls.sheet_names:
    try:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # Check if the DataFrame is empty
        if df.empty:
            print(f"The sheet '{sheet_name}' is empty.")
            continue
        
        # Append the DataFrame to the list
        all_data.append(df)
        
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
    except Exception as e:
        print(f"An error occurred while processing the sheet '{sheet_name}': {e}")

# Concatenate all the DataFrames in the list into a single DataFrame
all_data_df = pd.concat(all_data, ignore_index=True)

# Filter the all_data DataFrame for rt_type 'both' or 'import'
filtered_data = all_data_df[all_data_df['rt_type'].isin(['both', 'import'])]

# Group by 'vrf' and find the most common 'route_target' across all sheets
common_route_targets_overall = filtered_data.groupby('vrf')['route_target'].agg(lambda x: x.mode().iloc[0] if not x.empty else None)

# Check the most common RT in each sheet for each vrf
log_file = 'route_target_analysis_MC_AUP.log'
common_rt_per_sheet_dict = {}
with open(log_file, 'w') as f:
    # Check the most common RT in each sheet for each vrf
    common_rt_per_sheet_dict = {}
    for sheet_name in xls.sheet_names:
        try:
            # Initialize an empty dictionary for this sheet's common route targets
            common_rt_per_sheet_dict[sheet_name] = {}

            # Read the current sheet
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            # Check if the DataFrame is empty
            if df.empty:
                f.write(f"The sheet '{sheet_name}' is empty.\n")
                continue
            
            # Filter DataFrame for rt_type 'both' or 'import'
            df_filtered = df[df['rt_type'].isin(['both', 'import'])]
            
            # Group by 'vrf' and find the most common 'route_target' within the sheet
            if not df_filtered.empty:
                common_rt = df_filtered.groupby('vrf')['route_target'].agg(lambda x: x.mode().iloc[0] if not x.empty else None)
                common_rt_per_sheet_dict[sheet_name] = common_rt.to_dict()
            
        except Exception as e:
            f.write(f"An error occurred while processing the sheet '{sheet_name}': {e}\n")

    # Compare common RTs in each sheet with the overall common RTs
    for vrf, overall_common_rt in common_route_targets_overall.items():
        f.write(f"\nVRF: {vrf}, Overall Most Common Route-Target: {overall_common_rt}\n")
        for sheet_name in xls.sheet_names:
            sheet_vrfs = common_rt_per_sheet_dict.get(sheet_name, {}).keys()
            if vrf not in sheet_vrfs:
                f.write(f"Device '{sheet_name}' does not have VRF '{vrf}'.\n")
                continue

            # Get the common RT for the current VRF from the current sheet
            sheet_common_rt = common_rt_per_sheet_dict[sheet_name].get(vrf)
            if sheet_common_rt is None:
                f.write(f"Device '{sheet_name}' has VRF '{vrf}' but does not have a common Route-Target.\n")
            elif sheet_common_rt == overall_common_rt:
                f.write(f"Device '{sheet_name}' matches the overall Most Common Route-Target for VRF '{vrf}': {sheet_common_rt}\n")
            else:
                f.write(f"Device '{sheet_name}' has a different Route-Target for VRF '{vrf}': {sheet_common_rt} (expected {overall_common_rt})\n")

# The log has been saved to route_target_analysis.log
print(f"Analysis complete. Results have been saved to {log_file}")