import re
import pandas as pd

with open('KMPPR01-NCS5K-int.log') as file:
    file_contents = file.read()

# T = [line.split('\n') for line in open('KMPPR01-NCS5K-int.log').read().split('\n\n')]

# for element in T:
#     for i in element:
#         T =re.match("^([A-Za-z]*\d/\d+/\d+/\d+|^[A-Za-z-]*\d+)",i)
#         print(T)
my_list_int = []
my_list_state = []
my_list_IP =[]
my_list_Desc =[]
my_list_bundle =[]
my_list_bundle_1 =[]
my_dict = dict()
T= open('KMPPR01-NCS5K-int.log').read().split('\n\n')
for element in T:
    match = re.search(r"Description:(.*)",element)
    if match:
        my_list_Desc.append(match.group(0))
    else:
        my_list_Desc.append("NA")
    match = re.search(r"No. of members in this bundle: ([\s\S]*?) Last",element)
    if match:
        my_list_bundle.append(match.group(0))
    else:
        my_list_bundle.append("NA")
    inter = re.findall(r"^([A-Za-z]*\d/\d+/\d+/\d+|^[A-Za-z-]*\d+)",element)
    state = re.findall(r"is(.*)\sline protocol is (.*)",element)
    IP = re.findall(r"Internet address is(.*)",element)
    for i in inter:
        my_list_int.append(i)
    for s in state:
        my_list_state.append(s)
    for ip in IP:
        my_list_IP.append(ip)
my_list_Desc.pop(0)
my_list_bundle.pop(0)
for element in my_list_bundle:
    T = re.sub('(No. of members in this bundle:\s\d)|(Last)|(Full(.*))',"",element)
    my_list_bundle_1.append(T)

my_dict["interface"] = my_list_int
my_dict["state"] = my_list_state
my_dict["IP address"] = my_list_IP
my_dict["Description"] = my_list_Desc
my_dict["Bundle"] = my_list_bundle_1

dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in my_dict.items() })
writer = pd.ExcelWriter('converted-to-excel.xlsx')
dict_df.to_excel(writer)
writer.save()
print("DataFrame is exported successfully to 'converted-to-excel.xlsx' Excel File.")





# my_dict = dict(zip(my_list_int,my_list_state))
# print(my_dict)
# interface = re.compile(r"^([A-Za-z]*\d/\d+/\d+/\d+|^[A-Za-z-]*\d+)")

# int_list = []
# for i, line in enumerate(open("KMPPR01-NCS5K-int.log")):
#     for match in re.finditer(interface,line):
#         int_list.append(match.group())

# int_dic = {"interfaces":int_list}

# print(len(int_dic["interfaces"]))


# T = open("KMPPR01-NCS5K-int.log", "r")
# print(T.read())