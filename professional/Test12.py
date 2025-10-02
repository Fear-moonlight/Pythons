import json
import yaml
import os
import time

data_list = {"facts": [[[{"pint": "GigabitEthernet0/0/0/0", "hint": "GigabitEthernet0/0/0/0", "pname": "UER1"}, {"pint": "GigabitEthernet0/0/0/0", "hint": "GigabitEthernet0/0/0/1", "pname": "UER2"}, {"pint": "GigabitEthernet0/0/0/1", "hint": "GigabitEthernet0/0/0/2", "pname": "SR"}, {"pint": "GigabitEthernet0/0/0/0", "hint": "GigabitEthernet0/0/0/3", "pname": "PCE1"}, {"pint": "GigabitEthernet0/0/0/0", "hint": "GigabitEthernet0/0/0/4", "pname": "PCE2"}]]]}
data_mapping = {
    "SR": "222",
    "P": "200",
    "PCE1": "220",
    "PCE2": "221",
    "UER1": "201",
    "UER2": "202",
    "AGG01": "203",
    "AGG02": "204",
    "AGG03": "205",
    "AGG04": "206",
    "ACC11": "207",
    "ACC12": "208",
    "ACC13": "209",
    "ACC21": "210",
    "ACC22": "211",
    "ACC23": "212"
}

# Example usage for data_list["facts"][0]
if "facts" in data_list and isinstance(data_list["facts"], list):
    for data_item in data_list["facts"][0]:
        if isinstance(data_item, dict):
            pname = data_item.get("pname")
            if pname in data_mapping:
                data_item["ploopback_id"] = str(data_mapping[pname])

# Example usage for data_list["facts"][0][0]
if "facts" in data_list and isinstance(data_list["facts"], list):
    if isinstance(data_list["facts"][0], list):
        for data_item in data_list["facts"][0][0]:
            if isinstance(data_item, dict):
                pname = data_item.get("pname")
                if pname in data_mapping:
                    data_item["ploopback_id"] = str(data_mapping[pname])

result_dict = {}
for entry in data_list["facts"][0]:
    if isinstance(entry, dict):
        ploopback = entry['ploopback_id']
        hint = entry['hint']
        pint = entry['pint']
        pname = entry['pname']
        result_dict[hint] = (pint, pname,ploopback)
        parent_dict = {
            'my_dictionary': result_dict
        }
for entry in data_list["facts"][0][0]:
    if isinstance(entry, dict):
        ploopback = entry['ploopback_id']
        hint = entry['hint']
        pint = entry['pint']
        pname = entry['pname']
        result_dict[hint] = (pint, pname,ploopback)
        parent_dict = {
            'my_dictionary': result_dict
        }
print(parent_dict)