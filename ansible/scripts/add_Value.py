data = [
    {"pint": "GigabitEthernet0/0/0/0", "hint": "GigabitEthernet0/0/0/0", "pname": "RR1"},
    {"pint": "GigabitEthernet0/0/0/2", "hint": "GigabitEthernet0/0/0/2", "pname": "PE2"},
    {"pint": "GigabitEthernet0/0/0/1", "hint": "GigabitEthernet0/0/0/1", "pname": "PE3"}
]

for entry in data:
    if entry["pname"] == "PE2":
        entry["ploopback_id"] = "3"
    if entry["pname"] == "PE1":
        entry["ploopback_id"] = "2"
    if entry["pname"] == "PE3":
        entry["ploopback_id"] = "4"
    if entry["pname"] == "PE4":
        entry["ploopback_id"] = "5"
    if entry["pname"] == "RR1":
        entry["ploopback_id"] = "1"

print(data)