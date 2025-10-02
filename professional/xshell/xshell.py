import os
import openpyxl

# === CONFIGURATION ===
excel_file = "/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/professional/xshell/host_info.xlsx"        # Input Excel file
template_file = "/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/professional/xshell/Template.xsh"       # Your template XSH file
output_base = "/Users/aliesmaeilicharkhab/Documents/PersonalProjects/Python/professional/xshell/Sessions"             # Base output folder (you can set to Xshell Sessions folder)

# === LOAD EXCEL ===
wb = openpyxl.load_workbook(excel_file)
ws = wb.active  # assumes data is in the first sheet

# === READ TEMPLATE ===
with open(template_file, "r", encoding="utf-16") as f:
    template_content = f.read()

# === ITERATE ROWS ===
for row in ws.iter_rows(min_row=2, values_only=True):  # skip header
    hostname = row[0]   # Column A
    site_code = row[1]  # Column B
    ip_addr  = row[4]   # Column E (index 4 since Python is 0-based)

    if not (hostname and site_code and ip_addr):
        continue  # skip incomplete rows

    # Create subfolder for Site Code
    site_folder = os.path.join(output_base, site_code)
    os.makedirs(site_folder, exist_ok=True)

    # Customize template
    session_content = template_content.replace("<IP_Address>", str(ip_addr))
    session_content = session_content.replace("<Hostname>", str(hostname))

    # Save as Hostname.xsh in site folder
    output_file = os.path.join(site_folder, f"{hostname}.xsh")
    with open(output_file, "w", encoding="utf-16") as f:
        f.write(session_content)

    print(f"Created: {output_file}")

print("✅ All sessions created successfully.")
