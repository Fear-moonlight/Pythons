import pandas as pd
import sys

def showcommand_pe(efile,output):
    excel_data = pd.read_excel(efile)
    data = pd.DataFrame(excel_data, columns=['PointA','InterfaceA','Port-channelA', 'PointB', 'InterfaceB'])
    print("!")
    print("!!!!!!!WPJ_CORE!!!!!!!")
    print("!")
    for i in data.index:
        print("!")
        print("interface " + data['InterfaceA'][i])
        print(" description To " + data['PointB'][i] + " " + data['InterfaceB'][i])
        print(" medium p2p")
        print(" channel-group " + str(data['Port-channelA'][i]) + " mode active")
        print(" shutdown")


# def showcommand_pe(efile,output):
#     excel_data = pd.read_excel(efile)
#     data = pd.DataFrame(excel_data, columns=['PointA','InterfaceA','Port-channelA', 'PointB', 'InterfaceB', 'SR', 'SR_int'])
#     print("!")
#     print("!!!!!!!WPJ_CORE!!!!!!!")
#     print("!")
#     for i in data.index:
#         print("!")
#         print("interface " + data['InterfaceA'][i])
#         print(" description Core: " + data['PointB'][i] + data['InterfaceB'][i] + " [10Gbps]{L2VPN(" + data['SR'][i]+ data['SR_int'][i] + ")}")
#         print(" medium p2p")
#         print(" channel-group " + str(data['Port-channelA'][i]) + " mode active")
#         print(" shutdown")

output = 'showoutput'
efile = 'Var.xlsx'
sys.stdout = open(output,"w")
showcommand_pe(efile,output)
