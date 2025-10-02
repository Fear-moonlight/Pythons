from pyats.topology import loader
import pandas as pd

# Load the testbed
testbed = loader.load('testbed.yaml')

# Prefixes and devices to query
prefix_list = [
    "172.18.57.128/28",
    "172.18.57.144/28",
    "172.18.58.128/28",
    "172.18.58.144/28",
    "172.18.59.128/28",
    "172.18.59.144/28",
    "172.23.190.238/32",
    "172.27.0.1/32",
    "172.27.0.3/32",
    "172.27.0.5/32",
    "172.27.0.7/32",
    "172.27.0.9/32",
    "172.27.0.23/32"
]
Device_list = ["KRTUER01-ASR9K"]

# Use a context manager to handle the creation and saving of the Excel file
with pd.ExcelWriter('route_targets_1.xlsx', engine='openpyxl', mode='w') as excel_writer:
    # Iterate over each device
    for device_name in Device_list:
        device = testbed.devices[device_name]
        device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
        
        # List to hold all route target data for the device
        all_route_targets = []
        
        # Iterate over each prefix
        for prefix in prefix_list:
            command_prefix = f'show route vrf all ipv4 {prefix}'
            parsed_output = device.parse(command_prefix)
            
            # Iterate over each VRF
            for vrf in parsed_output['vrf']:
                command = f'show vrf {vrf} detail'
                parse_output_2 = device.parse(command)
                # Normalize the case to lowercase before accessing
                route_targets = parse_output_2[vrf]["address_family"].get("ipv4 unicast", {}).get("route_target", {})

                # Iterate over each route target
                for rt_key, rt_details in route_targets.items():
                    # Append route target information to the list
                    all_route_targets.append({
                        'Prefix': prefix,
                        'vrf': vrf,
                        'Route_target': rt_details['route_target'],
                        'RT Type': rt_details['rt_type']
                    })
            # for vrf in parsed_output['vrf']:
            #     command = f'show vrf {vrf} detail'
            #     parse_output_2 = device.parse(command)
            #     route_targets = parse_output_2[vrf]["address_family"]["ipv4 unicast"]["route_target"]
                
            #     # Iterate over each route target
            #     for rt_key, rt_details in route_targets.items():
            #         # Append route target information to the list
            #         all_route_targets.append({
            #             'Prefix': prefix,
            #             'vrf': vrf,
            #             'Route_target': rt_details['route_target'],
            #             'RT Type': rt_details['rt_type']
            #         })
        
        # Create a DataFrame from all route targets for the device
        df = pd.DataFrame(all_route_targets)
        
        # Write the DataFrame to a sheet named after the device in the Excel writer
        df.to_excel(excel_writer, sheet_name=device_name, index=False)
        
        # Disconnect from the device
        device.disconnect()