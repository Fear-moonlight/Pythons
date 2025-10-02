import os
import re
import ipaddress
import pandas as pd
from ciscoconfparse import CiscoConfParse
from collections import defaultdict

def extract_interface_ip_addresses(file_path):
    ip_addresses = []
    try:
        parse = CiscoConfParse(file_path, syntax='iosxr')
        interfaces = parse.find_objects(r"^interface\s")

        for interface in interfaces:
            shutdown_state = False
            ip_address = None

            for child in interface.children:
                if 'shutdown' in child.text:
                    shutdown_state = True
                elif 'ipv4 address' in child.text:
                    ip_line = child.text.strip()
                    if 'secondary' not in ip_line:
                        ip_address = ip_line.split()[2] + '/' + ip_line.split()[3]

            if ip_address:
                ip_addresses.append((ip_address, shutdown_state))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    return ip_addresses

# Function to process each configuration file
def process_files(directory):
    all_ip_addresses = defaultdict(list)

    # Walk through the directory to find all .txt files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                hostname = os.path.basename(file).replace('.txt', '')

                ip_list = extract_interface_ip_addresses(file_path)

                # Track all IP addresses and their hostnames
                for ip, shutdown in ip_list:
                    all_ip_addresses[ip].append((hostname, shutdown))

    return all_ip_addresses

# Function to save IP addresses to Excel file
def save_to_excel(all_ip_addresses):
    workbook = pd.ExcelWriter('ip_addresses.xlsx', engine='openpyxl')

    # Write each host's IP addresses to separate sheets
    for ip, hosts in all_ip_addresses.items():
        for hostname, shutdown in hosts:
            df = pd.DataFrame([(ip, 'Yes' if shutdown else 'No')], columns=['IP Address', 'Shutdown State'])
            df.to_excel(workbook, sheet_name=hostname, index=False)

    # Ensure at least one sheet is visible
    if not all_ip_addresses:
        df_empty = pd.DataFrame(columns=['IP Address', 'Shutdown State'])
        df_empty.to_excel(workbook, sheet_name='Empty', index=False)

    workbook.close()

    # Find duplicates and write to a new sheet
    duplicates = {ip: hosts for ip, hosts in all_ip_addresses.items() if len(hosts) > 1}
    if duplicates:
        data = []
        for ip, host_details in duplicates.items():
            hostnames = ', '.join([f"{hostname} (Shutdown: {'Yes' if shutdown else 'No'})" for hostname, shutdown in host_details])
            data.append({'IP Address': ip, 'Hostnames': hostnames})

        df_duplicates = pd.DataFrame(data)
        with pd.ExcelWriter('ip_addresses.xlsx', engine='openpyxl', mode='a') as writer:
            df_duplicates.to_excel(writer, sheet_name='Duplicates', index=False)

        print("Duplicate IP addresses have been written to the 'Duplicates' sheet in ip_addresses.xlsx.")
    else:
        print("No duplicate IP addresses found.")

# Function to check if an IP address is being used and by which host
def check_ip_address(all_ip_addresses, ip_address):
    results = []
    for ip, hosts in all_ip_addresses.items():
        if ip_address in ip:
            results.extend(hosts)
    return results

# Directory containing the nested folders with .txt files
directory =   '/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/professional/Duplicate/Config' # Update this path

# Process the files and get all IP addresses
all_ip_addresses = process_files(directory)

# Save the results to an Excel file
save_to_excel(all_ip_addresses)

# Interactive CLI to check IP addresses
print("Interactive IP Address Checker. Type 'exit' to quit.")
while True:
    ip_address = input("Enter IP address to check: ")
    if ip_address.lower() == 'exit':
        break
    results = check_ip_address(all_ip_addresses, ip_address)
    if results:
        print(f"IP address {ip_address} is being used by the following hosts:")
        for hostname, shutdown in results:
            print(f" - Hostname: {hostname}, Shutdown State: {'Yes' if shutdown else 'No'}")
    else:
        print(f"IP address {ip_address} is not being used by any host.")

