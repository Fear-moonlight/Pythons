from pyats.topology import loader
import pandas as pd
from genie.metaparser.util.exceptions import SchemaEmptyParserError


testbed = loader.load('testbed.yaml')
#prefix_list = ["172.18.57.144/28", "172.18.58.128/28", "172.18.58.128/28", "172.18.58.144/28", "172.18.59.128/28", "172.18.59.144/28", "172.27.0.1/32"]
prefix_list = [
    "10.63.168.0/24",
 ]   

device_list = ["KRTUER01-ASR9K", "KPGUER01-ASR9K", "60005-ALORSETAR-AGGA01", "70030-KPG-AGGA01", "70047-WPJ-AGGA01", "66013-IPOH-AGGA01", "63009-SEBERANGJAYA-AGGA01", "43146-SKUDAI-AGGA01", "40012-MER-AGGA01", "43165-KMP-AGGA01", "56000-KBX-AGGA01", "50005-SMBU-AGGA01", "BNTUER01-ASR9K", "WPJUER01-ASR9K", "SBUUER01-ASR9K", "SDKUER01-ASR9K", "KCHUER01-ASR9K", "SKDUER01-ASR9K", "SMBUER01-ASR9K", "KBAUER01-ASR9K", "SNWUER01-ASR9K", "KMPUER01-ASR9K", "IPHUER01-ASR9K", "SJYUER01-ASR9K", "ASRUER01-ASR9K", "MRIUER01-ASR9K", "INAUER01-ASR9K", "TAWUER01-ASR9K","KRTSR01-ASR9K", "KRTSR02-ASR9K", "KCHSR01-ASR9K", "KCHSR02-ASR9K","WPJSR01-ASR9K", "WPJSR02-ASR9K", "SHTSR01-ASR9K", "SHTSR02-ASR9K","KPGSR01-ASR9K", "KPGSR02-ASR9K"]

# Prepare to write to an Excel file
excel_file = 'route_targets_maxis_S1U_MOCN.xlsx'
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    for device_name in device_list:
        device = testbed.devices[device_name]
        try:
            print(f"Connecting to '{device}' ....")
            device.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
            print(f"Connection to '{device}' was successful")
            all_route_targets = []  # Initialize a list to store all route target data
            
            for prefix in prefix_list:
                try:
                    command_prefix = f'show route vrf all ipv4 {prefix}'
                    parsed_output = device.parse(command_prefix)
                    for vrf in parsed_output['vrf']:
                        try:
                            command = f'show vrf {vrf} detail'
                            parse_output_2 = device.parse(command)
                            route_targets = parse_output_2[vrf]["address_family"]["ipv4 unicast"]["route_target"]
                            for rt_key, rt_details in route_targets.items():
                                all_route_targets.append({
                                    'prefix': prefix,
                                    'vrf': vrf,
                                    'route_target': rt_details['route_target'],
                                    'rt_type': rt_details['rt_type']
                                })
                        except SchemaEmptyParserError:
                            print(f"No data found for 'show vrf {vrf} detail' on device {device_name}")
                        except Exception as e:
                            print(f"An error occurred while processing 'show vrf {vrf} detail': {e}")
                except SchemaEmptyParserError:
                    print(f"No data found for 'show route vrf all ipv4 {prefix}' on device {device_name}")
                except Exception as e:
                    print(f"An error occurred while processing 'show route vrf all ipv4 {prefix}': {e}")
            
            df = pd.DataFrame(all_route_targets)  # Convert list of route target data to a DataFrame
            df.to_excel(writer, sheet_name=device_name, index=False)  # Write DataFrame to an Excel sheet
        except Exception as e:
            print(f"An error occurred while connecting to device {device_name}: {e}")
        finally:
            device.disconnect()  # Ensure the device is disconnected even if an error occurred

print(f"Excel file '{excel_file}' has been created with the route target data.")