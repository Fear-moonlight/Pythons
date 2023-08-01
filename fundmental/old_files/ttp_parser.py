import json
import yaml
import os

result_dict = {}
result = open("cdp_outRR1.txt", "r")
data1 = result.read()
res = json.loads(data1)
for item in res['facts']:
    for nested_list in item:
        for entry in nested_list:
            hint = entry['hint']
            pint = entry['pint']
            pname = entry['pname']
            result_dict[hint] = (pint, pname)

parent_dict = {
    'my_dictionary': result_dict
}

def noalias_dumper(dumper, data):
    if isinstance(data, tuple):
        return dumper.represent_list(data)
    return dumper.represent_dict(data)

# Save the Ansible variable dictionary to a YAML file
with open('ansible_var_dict.yml', 'w', encoding='utf-8') as file:
    yaml.dump(parent_dict, file, default_flow_style=False, allow_unicode=True)


# my_dictionary = {
#     'facts': [
#         [
#             [{'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/0', 'pname': 'PE1'},
#              {'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/2', 'pname': 'PE3'},
#              {'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/1', 'pname': 'PE2'}]
#         ]
#     ]
# }
# for fact_list in my_dictionary['facts']:
#     for nested_list in fact_list:
#         for entry in nested_list:
#             hint = entry['hint']
#             pint = entry['pint']
#             pname = entry['pname']
#             result_dict[pint] = (hint, pname)

# print(result_dict)
