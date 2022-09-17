import pandas as pd
import sys

def showcommand_pe(efile,output):
    excel_data = pd.read_excel(efile)
    data = pd.DataFrame(excel_data, columns=['A(IP)','A(vrf)','B(IP)', 'B(vrf)'])
    print("!")
    print("!!!!!!!PE-SHOWCOMMAND!!!!!!!")
    print("!")
    for i in data.index:
        print("!")
        print("show bgp vrf " + data['A(vrf)'][i] + " summary")
        print("show bgp vrf " + data['A(vrf)'][i] + " neighbor " + data['B(IP)'][i] + " routes")
        print("show bgp vrf " + data['A(vrf)'][i] + " neighbor " + data['B(IP)'][i] + " advertised-routes")
        print("show bgp vrf " + data['A(vrf)'][i] + " neighbor " + data['B(IP)'][i] + " advertised-count")

def showcommand_ce(efile,output):
    excel_data = pd.read_excel(efile)
    data = pd.DataFrame(excel_data, columns=['A(IP)','A(vrf)','B(IP)', 'B(vrf)'])
    print("!")
    print("!!!!!!!CE-SHOWCOMMAND!!!!!!!")
    print("!")
    for i in data.index:
        print("!")
        print("show bgp vrf " + data['B(vrf)'][i] + " all summary")
        print("show bgp vrf " + data['B(vrf)'][i] + " all neighbor " + data['A(IP)'][i] + " routes")
        print("show bgp vrf " + data['B(vrf)'][i] + " allneighbor " + data['A(IP)'][i] + " advertised-routes")
        
def bgp_pe(efile,output):
    excel_data = pd.read_excel(efile)
    data = pd.DataFrame(excel_data, columns=['A(IP)','A(vrf)','B(IP)', 'B(vrf)'])
    print("!")
    print("!!!!!!!PE-CONFIGURATION!!!!!!!!")
    print("!")
    print("router bgp 65535")
    for i in data.index:
        print("vrf " + data['A(vrf)'][i])
        print("   neighbor  " + data['B(IP)'][i])
        print("     password clear C3lc@m_CSW")
        print("!")
        
def bgp_ce_xe(efile,output):
    excel_data = pd.read_excel(efile)
    data = pd.DataFrame(excel_data, columns=['A(IP)','A(vrf)','B(IP)', 'B(vrf)'])
    print("!!!!!!!CE-CONFIGURATION!!!!!!!!")
    print("!")
    print("router bgp 65111")
    for i in data.index:
        print("address-family ipv4 vrf  " + data['B(vrf)'][i])
        print("   neighbor  " + data['A(IP)'][i] + " password 0 C3lc@m_CSW")
        print("!")


output = 'showoutputxe'
efile = 'BGP_PE_CE_XE.xlsx'
sys.stdout = open(output,"w")
showcommand_pe(efile,output)
showcommand_ce(efile,output)
bgp_pe(efile,output)
bgp_ce_xe(efile,output)