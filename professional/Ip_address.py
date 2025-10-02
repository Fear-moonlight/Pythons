import ipaddress

# Define the base IP network
base_network = ipaddress.IPv4Network("10.150.14.0/23")

# Calculate the /31 subnets and list them
for subnet in base_network.subnets(new_prefix=31):
    print(subnet)