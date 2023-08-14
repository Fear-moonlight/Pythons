import json
import yaml
import os
import time

source_directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/output/cdp_output'
target_directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/host_vars'

def update_data_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    data_list = json.loads(content)
    for data in data_list["facts"][0][0]:
        if data["pname"] == "PE1":
            data["ploopback_id"] = "2"
        elif data["pname"] == "PE2":
            data["ploopback_id"] = "3"
        elif data["pname"] == "PE3":
            data["ploopback_id"] = "4"
        elif data["pname"] == "RR1":
            data["ploopback_id"] = "1"

    with open(file_path, "w") as file:
        file.write(json.dumps(data_list, ensure_ascii=False, indent=4))

def process_file(source_file_path, target_directory):
    file_name = os.path.basename(source_file_path)
    target_file_name = os.path.splitext(file_name)[0] + '.yml'
    target_path = os.path.join(target_directory, os.path.splitext(file_name)[0])
    target_file_path = os.path.join(target_path, target_file_name)

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    with open(source_file_path, 'r') as source_file:
        time.sleep(5)
        data = json.load(source_file)
        result_dict = {}

        for item in data['facts']:
            for nested_list in item:
                for entry in nested_list:
                    ploopback = entry.get('ploopback_id', '')
                    hint = entry.get('hint', '')
                    pint = entry.get('pint', '')
                    pname = entry.get('pname', '')
                    result_dict[hint] = (pint, pname, ploopback)

        parent_dict = {'my_dictionary': result_dict}

    def noalias_dumper(dumper, data):
        if isinstance(data, tuple):
            return dumper.represent_list(data)
        return dumper.represent_dict(data)

    with open(target_file_path, 'w') as target_file:
        yaml.dump(parent_dict, target_file, default_flow_style=False, allow_unicode=True, Dumper=yaml.SafeDumper)

if os.path.exists(source_directory_path) and os.path.isdir(source_directory_path):
    for filename in os.listdir(source_directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(source_directory_path, filename)
            update_data_in_file(file_path)
else:
    print("Directory path does not exist or is not a directory.")

file_list = os.listdir(source_directory_path)

for file_name in file_list:
    source_file_path = os.path.join(source_directory_path, file_name)
    if os.path.isfile(source_file_path) and file_name.endswith('.txt'):
        print("Converting file:")
        process_file(source_file_path, target_directory_path)
