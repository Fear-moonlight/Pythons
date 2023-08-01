import os
import json

directory_path = '/Users/aliesmaeilicharkhab/Documents/Personal Projects/Python/ansible/output/cdp_output'

def update_data_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    data_list = json.loads(content)
    for data in data_list["facts"][0][0]:
        if data["pname"] == "PE1":
            data["ploopback_id"] = "2"
        if data["pname"] == "PE2":
            data["ploopback_id"] = "3"
        if data["pname"] == "PE3":
            data["ploopback_id"] = "4"
        if data["pname"] == "PE4":
            data["ploopback_id"] = "5"
        if data["pname"] == "RR1":
            data["ploopback_id"] = "1"
    with open(file_path, "w") as file:
        file.write(json.dumps(data_list, ensure_ascii=False, indent=4))

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            update_data_in_file(file_path)
else:
    print("Directory path does not exist or is not a directory.")
