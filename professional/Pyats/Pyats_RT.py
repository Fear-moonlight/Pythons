from pyats.topology import loader
import re
from genie.libs.parser.utils import get_parser
import csv
import time
from collections import Counter

def extract_rt_values(raw_output):
    pattern = r"Path #1:.*?Extended community:.*?(RT:[\S\s]*?)\n"
    matches = re.findall(pattern, raw_output, re.DOTALL)
    if matches:
        rt_values = re.findall(r"RT:(\S+)", matches[0])
        return rt_values
    else:
        return []

testbed = loader.load('testbed.yaml')
# device = testbed.devices['KPGUER01-ASR9K']
# def reconnect_device(device):
#     if not device.is_connected():
#         device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
# reconnect_device(device)
# output = device.execute('show version')

# print(output)
device = testbed.devices['KPGUER01-ASR9K']

# Connect to the device with the specified parameters
device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

parsed_output = device.parse('show bgp vrf maxis_S1U_MOCN')
print(parsed_output)
# for prefix in parsed_output['vrf']['maxis_mc_acp']['address_family']['ipv4_unicast']['prefix']:
#     #print(prefix)
#         command = 'show bgp vrf maxis_MC_ACP ipv4 unicast ' + prefix
#         prefix_output = device.parse(command)
#with open('prefix_outputs.txt', 'w') as output_file:
    # Iterate over each prefix in the parsed output
all_rt_values = []
with open('bgp_rt_values_maxis_S1U_MOCN.csv', mode='w', newline='') as csv_file:
    fieldnames = ['VRF name', 'Prefix', 'RT values']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()

    for prefix, prefix_data in parsed_output['vrf']['maxis_s1u_mocn']['address_family']['ipv4_unicast']['prefix'].items():
        command = f'show bgp vrf maxis_S1U_MOCN ipv4 unicast {prefix}'
        raw_output = device.execute(command)
        rt_values = extract_rt_values(raw_output)
        rt_values_str = ', '.join(rt_values)
        all_rt_values.extend(rt_values)
        writer.writerow({'VRF name': 'maxis_S1U_MOCN', 'Prefix': prefix, 'RT values': rt_values_str})
   
        # Construct the command for each prefix
    #     try:
    #         command = f'show bgp vrf maxis_MC_ACP ipv4 unicast  {prefix}'
        
    #     # Execute the command to get the raw output
    #     #raw_output = device.execute(command)
    # #         parsed_output_1 = device.parse(command)
    # #     # Write the prefix and its raw output to the file
    # #         output_file.write(f'Prefix: {prefix}\n')
    # #    # output_file.write(f'Raw Output:\n{raw_output}\n')
    # #         output_file.write(f'Raw Output:\n{parsed_output_1}\n')
    # #         output_file.write('-' * 60 + '\n\n')  # Write a separator line
    # #     except UnboundLocalError as e:
    # #         print(f"An error occurred: {e}. Reconnecting and retrying.")
    # #         reconnect_device(device)
    # #         # Retry the command after reconnecting
    # #         prefix_parsed_output = device.parse(command)
    # #         output_file.write(f'Prefix: {prefix}\n')
    # #         output_file.write(f'Parsed Output:\n{prefix_parsed_output}\n')
    # #         output_file.write('-' * 60 + '\n\n')
    #         prefix_parsed_output = device.parse(command)
            
    #         # Write the prefix and its parsed output to the file
    #         output_file.write(f'Prefix: {prefix}\n')
    #         output_file.write(f'Parsed Output:\n{prefix_parsed_output}\n')
    #         output_file.write('-' * 60 + '\n\n')  # Write a separator line
    #     except Exception as e:
    #         print(f"An error occurred: {e}. Reconnecting and retrying.")
    #         reconnect_device(device)
    #         # Retry the command after reconnecting
    #         prefix_parsed_output = device.parse(command)
    #         output_file.write(f'Prefix: {prefix}\n')
    #         output_file.write(f'Parsed Output:\n{prefix_parsed_output}\n')
    #         output_file.write('-' * 60 + '\n\n')

device.disconnect()

counter = Counter(all_rt_values)
most_common_rt = counter.most_common()

# Display the most common RT values
print("The most common RT values are:")
for rt, count in most_common_rt:
    print(f"{rt}: {count} occurrences")