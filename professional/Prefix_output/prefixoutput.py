import re

def parse_bgp_advertised_routes(file_path, prefix_list):
    # Read the file content
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract prefixes from the output lines (assuming prefixes are at the start of lines)
    # Example prefix format: 183.171.0.0/16
    advertised_prefixes = re.findall(r'^(\d{1,3}(?:\.\d{1,3}){3}/\d{1,2})', content, re.MULTILINE)

    # Check which prefixes from prefix_list are in advertised_prefixes
    matched_prefixes = [prefix for prefix in prefix_list if prefix in advertised_prefixes]

    if matched_prefixes:
        print("The following prefixes from your list are advertised:")
        for p in matched_prefixes:
            print(f" - {p}")
    else:
        print("No prefixes from your list are advertised.")

if __name__ == "__main__":
    # Example usage
    file_path = 'bgp_output2.txt'  # Path to your text file with BGP output
    # List of prefixes to check
    prefixes_to_check = [
    '183.171.112.0/22',
    '183.171.116.0/22',
    '183.171.176.0/24',
    '183.171.183.0/24',
    '183.171.248.0/24',
    '183.171.249.0/24',
    '183.171.120.0/22',
    '183.171.124.0/22',
    '183.171.177.0/24',
    '183.171.184.0/24',
    '183.171.240.0/24',
    '183.171.241.0/24',
    '183.171.242.0/24',
    '183.171.186.0/24',
    '183.171.205.0/24',
    '183.171.158.0/24',
    '183.171.156.0/24'
        # Add more prefixes as needed
    ]

    parse_bgp_advertised_routes(file_path, prefixes_to_check)