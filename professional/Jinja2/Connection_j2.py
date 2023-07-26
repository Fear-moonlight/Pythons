from platform import platform
from netmiko import Netmiko
import time
import ttp
import getpass
import pandas as pd
from yaml import safe_load
import pprint
from jinja2 import Environment, FileSystemLoader
from xlsxwriter import Workbook
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

# def send_cmd(conn,command):
#     """
#     give an open connection and a command , issue the command and wait 1 second for command to
#     be processd 
#     """
#     output = conn.send(command + "\n")
#     time.sleep(1.0)
#     return output

# def get_output(conn):
#     """
#     given an open connection , read all the data from the buffer and decode the bytes string
#     as utf-8
#     """
#     return conn.recv(65535).decode("utf-8")
wb=Workbook("New File.xlsx")
passwd =getpass.getpass("please enter your password:")
def main():
    """
    excutation starts here.
    """
    # Read the hosts file into structured data, may raise YAMLError
    with open("Host.yml","r") as handle:
        host_root = safe_load(handle)
    # Iterate over the list of hosts(list of dictionaries)
    platfrom_map ={"ios":"cisco_ios", "iosxr":"cisco_xr"}

    for host in host_root["host_list"]:
        platform = platfrom_map[host["platform"]]

        # Load the host-speific vrf declarative state
        with open(f"vars/{host['name']}_vrfs.yml","r") as handle:
            vrfs = safe_load(handle)
    # Setup the Jinja2 templating enviroment and render the template
        J2_env = Environment(
            loader=FileSystemLoader("."), trim_blocks=True, autoescape=True
        )
        template = J2_env.get_template(
            f"templates/netmiko/cisco_xr.j2"
        )
        new_vrf_config = template.render(data=vrfs)
    # create paramiko SSH Client to connect to the device
        conn = Netmiko(
            host = host["name"],
            username = "cisco",
            password = passwd,
            device_type = "cisco_xr",
            ssh_config_file= "~/.ssh/config",
        )
        commands =["terminal lenght 0", "show run", "show int","show ip int br"]
        # send the configuration string to the device
        # result = conn.send_config_set(new_vrf_config.split("\n"))
        show_int = conn.send_command("show int", expect_string="#", use_ttp=True, ttp_template="templates/ttp/show_interface.ttp")
        show_ospf_nei = conn.send_command("show ospf neighbor detail", expect_string="#", use_ttp=True, ttp_template="templates/ttp/show_ospf_nei.ttp")
        #result = conn.send_command("show int", expect_string="#", read_timeout=10)
        print(show_int)
        print(show_ospf_nei)
        int_ordered_list=["interface", "link_status", "protocol_status", "IP_address"]
        ospf_ordered_list=["router_id", "int_add", "int_name", "area_id", "state_changes","ospf_state","ospf_pri"]
        wb=Workbook(host["name"]+".xlsx")
        ws=wb.add_worksheet("show_int")
        first_row=0
        for header in int_ordered_list:
            col=int_ordered_list.index(header)
            ws.write(first_row,col,header)
        row=1
        for elementss in show_int:
           for elements in elementss:
                for element in elements:
                    for _key,_value in element.items():
                        col=int_ordered_list.index(_key)
                        ws.write(row,col,_value)
                    row+=1 
        ws=wb.add_worksheet("show_ospf")
        first_row=0
        for header in ospf_ordered_list:
            col=ospf_ordered_list.index(header)
            ws.write(first_row,col,header)
        row=1
        for elementss in show_ospf_nei:
           for elements in elementss:
                for element in elements:
                    for _key,_value in element.items():
                        col=ospf_ordered_list.index(_key)
                        ws.write(row,col,_value)
                    row+=1 
        wb.close()
        #ordered_list=["interface", "link_status", "protocol_status", "IP_address"]
        #wb=Workbook(host["name"]+".xlsx")
        #ws=wb.add_worksheet(host["name"])
        #first_row=0
        #for header in ordered_list:
        #    col=ordered_list.index(header)
        #    ws.write(first_row,col,header)
        #row=1
        #for elementss in result:
        #    for elements in elementss:
        #        for element in elements:
        #            for _key,_value in element.items():
        #                col=ordered_list.index(_key)
        #                ws.write(row,col,_value)
        #            row+=1 
        #wb.close()
        # file = open(f"{host['name']}_log.txt","w")
        # file.write(result)
        # file.close()
        # result_list=[]
        # for command in commands:
        #     result = conn.send_command(command)
        # # print(result)
        #     file = open(f"{host['name']}_log.txt","a")
        #     file.write(str(result))
        #     file.close()
        conn.disconnect()
if __name__ == "__main__":
    main()