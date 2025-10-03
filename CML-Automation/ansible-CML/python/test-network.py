from virl2_client import ClientLibrary
import sys

CML_SERVER = "https://10.1.1.20"
LAB_FILE = "ansible-test-lab.yaml"
CML_USER = "admin"
CML_PASS = "1234QWer"
LAB_NAME = "Test Network" 

client = ClientLibrary(CML_SERVER, CML_USER, CML_PASS, ssl_verify=False)

def start_network():
    try:
        # Load the lab from a local file
        with open(LAB_FILE, "r") as lab_file:
            lab = client.import_lab(lab_file.read())

        print("Lab created successfully!")
        print("Starting nodes...")
        # Start the lab
        lab.start()

        print("Lab started successfully!")
        print("Lab ID:", lab.id)
    except Exception as e:
        print("An error occurred:", str(e))

def remove_network():
    try:
        print(f"Checking if '{LAB_NAME}' exists for removal...")
        for lab in client.find_labs_by_title(LAB_NAME):
            print(f"Removing {lab}")
            lab.stop()
            lab.wipe()
            lab.remove()
            print("Lab removed successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [up/down]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "up":
        start_network()
    elif action == "down":
        remove_network()
    else:
        print("Invalid argument. Use 'up' to start the network or 'down' to remove it.")
        sys.exit(1)