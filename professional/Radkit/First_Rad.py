from radkit_client import create_context, sso_login
import radkit_genie
from ttp import ttp
import pandas as pd

ttp_template = """
interface {{ interface }}
 ipv4  address {{ ip }} {{ mask}}
 description {{ description }}
 ip vrf {{ vrf }}
"""

def _run_code():
    # Ask for user input.
    #email = input("email> ")
    #domain = input("domain> ")
    #service_serial = input("service serial> ")

    # Connect to the given service, using SSO login.
    client = sso_login("aesmaeil@cisco.com")
    service = client.service("u9em-v3xz-7jwy").wait()
    # pe1= service.inventory['pe1']
    # req = pe1.exec("show run").wait()
    # show_run = req.result.text
    # parser = ttp(data=show_run,template =ttp_template)
    # parser.parse()
    # results = parser.result(format='json')[0]
    all_pe = service.inventory.filter("name","pe")
    for i in all_pe:
        #print(service.inventory[i].exec("show route").wait().result.data)
        if "Routing entry for 99.99.99.99/32" in service.inventory[i].exec("show route 99.99.99.99/32").wait().result.data:
            print (i)
    for i in all_pe:
        show_run = service.inventory[i].exec("show run").wait().result.text
        parser = ttp(data=show_run,template =ttp_template)
        parser.parse()
        result = parser.result(format ='json')[0]
        #print(result)
        pd_object = pd.read_json(result, orient='records')
        pd_object.to_excel('output', sheet_name='sheet1', index=False)




def main():
    with create_context():
        _run_code()


if __name__ == "__main__":
    main()