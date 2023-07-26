from xlsxwriter import Workbook
list = [[[{'IP_address': '192.168.0.1/32', 'interface': 'Loopback0', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': 'Unknown', 'interface': 'Null0', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': '10.1.2.1/24', 'interface': 'GigabitEthernet0/0/0/0', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': '10.1.3.1/24', 'interface': 'GigabitEthernet0/0/0/1', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': '10.1.4.1/24', 'interface': 'GigabitEthernet0/0/0/2', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': '10.1.5.1/24', 'interface': 'GigabitEthernet0/0/0/3', 'link_status': 'up', 'protocol_status': 'up'}, {'IP_address': '10.12.15.29/24', 'interface': 'GigabitEthernet0/0/0/4', 'link_status': 'up', 'protocol_status': 'up'}]]]
list_1 = [[[{'ospf_pri': '1', 'ospf_state': 'FULL', 'state_changes': '6', 'area_id': '0', 'int_name': 'GigabitEthernet0/0/0/0', 'router_id': '192.168.0.1', 'int_add': '10.1.2.1'}, {'ospf_pri': '1', 'ospf_state': 'FULL', 'state_changes': '6', 'area_id': '0', 'int_name': 'GigabitEthernet0/0/0/1', 'router_id': '192.168.0.3', 'int_add': '10.2.3.3'}, {'ospf_pri': '1', 'ospf_state': 'FULL', 'state_changes': '6', 'area_id': '0', 'int_name': 'GigabitEthernet0/0/0/2', 'router_id': '192.168.0.4', 'int_add': '10.2.4.4'}, {'ospf_pri': '1', 'ospf_state': 'FULL', 'state_changes': '6', 'area_id': '0', 'int_name': 'GigabitEthernet0/0/0/3', 'router_id': '192.168.0.5', 'int_add': '10.2.5.5'}]]]

int_ordered_list=["interface", "link_status", "protocol_status", "IP_address"]
ospf_ordered_list=["router_id", "int_add", "int_name", "area_id", "state_changes","ospf_state","ospf_pri"]
def write_excel(x,y,z):
    ws=wb.add_worksheet(x)
    first_row=0
    for header in y:
        col=y.index(header)
        ws.write(first_row,col,header)
    row=1
    for elementss in z:
       for elements in elementss:
            for element in elements:
                for _key,_value in element.items():
                    col=y.index(_key)
                    ws.write(row,col,_value)
                row+=1 

wb=Workbook("New File.xlsx")
write_excel("show_int",int_ordered_list,list)
#ws=wb.add_worksheet("show_int")
#first_row=0
#for header in int_ordered_list:
#    col=int_ordered_list.index(header)
#    ws.write(first_row,col,header)
#row=1
#for elementss in list:
#   for elements in elementss:
#        for element in elements:
#            for _key,_value in element.items():
#                col=int_ordered_list.index(_key)
#                ws.write(row,col,_value)
#            row+=1 
#ws=wb.add_worksheet("show_ospf")
#first_row=0
#for header in ospf_ordered_list:
#    col=ospf_ordered_list.index(header)
#    ws.write(first_row,col,header)
#row=1
#for elementss in list_1:
#   for elements in elementss:
#        for element in elements:
#            for _key,_value in element.items():
#                col=ospf_ordered_list.index(_key)
#                ws.write(row,col,_value)
#            row+=1 
wb.close()


