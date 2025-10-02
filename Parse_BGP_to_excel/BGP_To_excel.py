import csv
import re

input_file = "/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/Parse_BGP_to_excel/IPv6_KCH_CSW_CORE_Routes_2914_1.log"
output_file = "bgp1.csv"

prefix_line = re.compile(
    r'^[\*\> ]*[\w]*?([\da-fA-F:\/]+)\s+([\da-fA-F:]+)(?:\s+(\d+)\s+(\d+)?\s+(\d+)?\s+(.*))?$'
)

# Match continuation line (wrapped metric/locprf/weight/path)
path_line = re.compile(r'^\s+(\d+)\s+(\d+)?\s+(\d+)?\s+(.*)$')

rows = []
current_entry = {}

with open(input_file, "r") as f:
    for line in f:
        line = line.rstrip()

        # Try match prefix line
        m = prefix_line.match(line)
        if m:
            # save previous entry if complete
            if current_entry and "AS_Path" in current_entry:
                rows.append(current_entry)

            current_entry = {
                "Network": m.group(1),
                "NextHop": m.group(2),
                "Metric": m.group(3) or "",
                "LocPrf": m.group(4) or "",
                "Weight": m.group(5) or "",
                "AS_Path": "",
                "Origin": ""
            }

            if m.group(6):  # path is already on the same line
                parts = m.group(6).split()
                if parts[-1] in ["i", "e", "?"]:
                    current_entry["Origin"] = parts[-1]
                    current_entry["AS_Path"] = " ".join(parts[:-1])
                else:
                    current_entry["AS_Path"] = " ".join(parts)
                rows.append(current_entry)
                current_entry = {}
            continue

        # Match wrapped path line
        m = path_line.match(line)
        if m and current_entry:
            current_entry["Metric"] = m.group(1)
            current_entry["LocPrf"] = m.group(2) or ""
            current_entry["Weight"] = m.group(3) or ""
            parts = (m.group(4) or "").split()
            if parts and parts[-1] in ["i", "e", "?"]:
                current_entry["Origin"] = parts[-1]
                current_entry["AS_Path"] = " ".join(parts[:-1])
            else:
                current_entry["AS_Path"] = " ".join(parts)
            rows.append(current_entry)
            current_entry = {}

# Write CSV
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Network", "NextHop", "Metric", "LocPrf", "Weight", "AS_Path", "Origin"])
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Done! Saved {len(rows)} routes into {output_file}")