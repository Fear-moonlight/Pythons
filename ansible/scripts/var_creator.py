import json
import yaml
import os
import time
directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/output/cdp_output'

def update_data_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        time.sleep(5)
    data_list = json.loads(content)
    for data in data_list["facts"][0][0]:
        if data["pname"] == "PE1":
            data["ploopback_id"] = str("2")
        if data["pname"] == "PE2":
            data["ploopback_id"] = str("3")
        if data["pname"] == "PE3":
            data["ploopback_id"] = str("4")
        if data["pname"] == "RR1":
            data["ploopback_id"] = str("1")
    with open(file_path, "w") as file:
        file.write(json.dumps(data_list, ensure_ascii=False, indent=4))

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            update_data_in_file(file_path)
else:
    print("Directory path does not exist or is not a directory.")

source_directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/output/cdp_output'
target_directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/host_vars'
def process_file(source_file_path,target_directory):
    file_name = os.path.basename(source_file_path)
    target_file_name = os.path.splitext(file_name)[0] + '.yml'
    target_path = target_directory  + "/" + os.path.splitext(file_name)[0]
    target_file_path = os.path.join(target_path,target_file_name)
    if os.path.exists(target_path) is False:
                os.mkdir(target_path)
    with open(source_file_path, 'r') as source_file:
        time.sleep(5)
        result_dict = {}
        print(source_file)      
        data1 = source_file.read()
        res = json.loads(data1)
        for item in res['facts']:
            for nested_list in item:
                for entry in nested_list:
                    ploopback = entry['ploopback_id']
                    hint = entry['hint']
                    pint = entry['pint']
                    pname = entry['pname']
                    result_dict[hint] = (pint, pname,ploopback)

        parent_dict = {
            'my_dictionary': result_dict
        }

    def noalias_dumper(dumper, data):
        if isinstance(data, tuple):
            return dumper.represent_list(data)
        return dumper.represent_dict(data)
            
    print(parent_dict)
    with open(target_file_path, 'w') as target_file:
        yaml.dump(parent_dict, target_file, default_flow_style=False, allow_unicode=True,Dumper=yaml.SafeDumper)


file_list = os.listdir(source_directory_path)

for file_name in file_list:
    source_file_path = os.path.join(source_directory_path, file_name)
    if os.path.isfile(source_file_path) and file_name.endswith('.txt'):
        print("Converting file:")
        process_file(source_file_path, target_directory_path)
        # print(f"File '{file_name}' converted to YAML and saved in target directory.\n")


# def noalias_dumper(dumper, data):
#     if isinstance(data, tuple):
#         return dumper.represent_list(data)
#     return dumper.represent_dict(data)

# # Save the Ansible variable dictionary to a YAML file
# with open('ansible_var_dict.yml', 'w', encoding='utf-8') as file:
#     yaml.dump(parent_dict, file, default_flow_style=False, allow_unicode=True)


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
