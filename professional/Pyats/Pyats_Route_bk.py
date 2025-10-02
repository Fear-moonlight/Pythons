from pyats.topology import loader
import re
from genie.libs.parser.utils import get_parser
import csv
import time
from collections import Counter


testbed = loader.load('testbed.yaml')
prefix_list = ["172.18.57.144/28", "172.18.58.128/28"]
Device_list = ["KRTUER01-ASR9K"]
for device in Device_list:
    device1 = testbed.devices[device]

    device1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)
    for prefix in prefix_list:
        command_prefix = f'show route vrf all ipv4 {prefix}'
        parsed_output = device1.parse(command_prefix)
        for vrf in parsed_output['vrf']:
            print(vrf)
            command = f'show vrf {vrf} detail'
            # parse_output_1 = device.parse(command)
            # print(parse_output_1)
            parse_output_2 = device1.parse(command)
            #route_targets = parse_output_2[vrf]["address_family"]["ipv4 unicast"]["route_target"]
            route_targets = parse_output_2['E_Iu_CP']['address_family']['ipv4 unicast']['route_target']
            #print(route_targets)
            extracted_info = []
            for rt_key, rt_details in route_targets.items():
                extracted_info.append({
                    'route_target': rt_details['route_target'],
                    'rt_type': rt_details['rt_type']
                })
            for item in extracted_info:
                print(f"Route Target: {item['route_target']}, RT Type: {item['rt_type']}")

            # for key, rt_info in route_targets.items():
            #     print(f"Route Target: {rt_info['route_target']}, RT Type: {rt_info['rt_type']}")
device1.disconnect()

