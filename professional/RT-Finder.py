import re

# Sample output
output = """show bgp vrf maxis_MC_ACP ipv4 unicast 10.31.19.185/32

Thu Jun  6 10:54:34.924 MYT
BGP routing table entry for 10.31.19.185/32, Route Distinguisher: 10.159.255.5:106
Versions:
  Process           bRIB/RIB  SendTblVer
  Speaker         1021595822  1021595822
Last Modified: May 31 00:48:54.516 for 6d10h
Paths: (1 available, best #1)
  Advertised to CE peers (in unique update groups):
    10.151.81.221   
  Path #1: Received by speaker 0
  Advertised to CE peers (in unique update groups):
    10.151.81.221   
  Local, (Received from a RR-client)
    10.240.100.94 (metric 11) from 10.240.100.94 (10.240.100.94)
      Received Label 33191 
      Origin incomplete, metric 0, localpref 100, weight 10000, valid, internal, best, group-best, import-candidate, imported
      Received Path ID 0, Local Path ID 1, version 1021595822
      Extended community: RT:65535:11250 RT:65535:60900 RT:65535:60902 RT:65535:60904 RT:65535:66361 
      Source AFI: VPNv4 Unicast, Source VRF: default, Source Route Distinguisher: 10.240.100.94:9"""

# Define a regular expression pattern to extract the RT values from the best path
pattern = r"Path #1:.*?Extended community:.*?(RT:[\S\s]*?)\n"

# Find all matches of the RT values in the output
matches = re.findall(pattern, output, re.DOTALL)

# Since the regex includes "Path #1", which indicates the best path, we should only get one match
if matches:
    # Extract the RT values
    rt_values = re.findall(r"RT:(\S+)", matches[0])
    print("RT values from the best path are:", rt_values)
else:
    print("No RT values found for the best path.")