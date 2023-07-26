import paramiko
import time
# host_collection =[R1,R2]
# for host in host_collection:
#     conn = "new paramiko SSHclient to host"
#     vrf_config = conn.send("os specific vrf command")
#     with open(host specific file ) as handle:
#         handle.write(vrf_config)

# conn_params = paramiko.SSHClient()
# conn_params.connect(
#     hostname ="R1",
#     username ="pyuser",
#     password ="bypass",
# )
# conn = conn_params.invoke_shell()
# conn.send("show ip int br\n")
# # we may need to wait
# output = conn.recv(65535)
# # we may want to convert from bytes

def send_cmd(conn,command):
    """
    give an open connection and a command , issue the command and wait 1 second for command to
    be processd 
    """
    conn.send(command + "\n")
    time.sleep(1.0)
def get_output(conn):
    """
    given an open connection , read all the data from the buffer and decode the bytes string
    as utf-8
    """
    return conn.recv(65535).decode("utf-8")

def main():
    """
    excutation starts here.
    """
    # define host inventory in line, remember our platform types
    # R1 is a cisco IOS-XE CSR1000V
    # R2 is a cisco IOS-XR XRv9000
    host_dict = {
        "R1":"show running-config | section vrf",
        "R2":"show running-config vrf",
    }
    # for each host in the inventory dict, extract key and value
    for hostname, vrf_cmd in host_dict.items():
        conn_params = paramiko.SSHClient()
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.connect(       
            hostname=hostname,
            port=22,
            username="V06519X",
            password="Abol^76377",
            look_for_keys= False,
            allow_agent=False,
        )
          
        # Get an interactive shell and wait a bit for the prompt to appear
        conn = conn_params.invoke_shell()
        time.sleep(1.0)
        #print(f"Logged into {get_output(conn).strip()} succesfully")

        commands =[
            "terminal length 0",
            "show version | include software",
            vrf_cmd,
        ]
        concat_output = ""
        for command in commands:
            #it helps to have a custom fuction to abstract sending 
            #commands and reading output from device
            send_cmd(conn,command)
            concat_output += get_output(conn)
        # Close session when we are done
        conn.close()
        print(f"Writing {hostname} facts to file")
        with open(f"{hostname}_facts","w") as handle:
            handle.write(concat_output)

if __name__ == "__main__":
    main()