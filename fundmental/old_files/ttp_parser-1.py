import yaml

my_dictionary = {
    'facts': [
        [
            [{'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/0', 'pname': 'PE1'},
             {'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/2', 'pname': 'PE3'},
             {'hint': 'GigabitEthernet0/0/0/0', 'pint': 'GigabitEthernet0/0/0/1', 'pname': 'PE2'}]
        ]
    ]
}

# Remove the `!!python/tuple` tag from the YAML output
def noalias_dumper(dumper, data):
    if isinstance(data, tuple):
        return dumper.represent_scalar('tag:yaml.org,2002:str', str(data))
    return dumper.represent(data)

yaml.add_representer(tuple, noalias_dumper)

# Convert dictionary to YAML format
yaml_string = yaml.dump(my_dictionary, default_flow_style=False, allow_unicode=True)

# Write the YAML string to a file
with open('output_file.yml', 'w', encoding='utf-8') as file:
    file.write(yaml_string)