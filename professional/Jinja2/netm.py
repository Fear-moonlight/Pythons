import jinja2
from yaml import safe_load
with open(f"vars/PE1_vrfs.yml","r") as handle:
    vrfs = safe_load(handle)
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "templates/netmiko/cisco_xr.j2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(data=vrfs)  # this is where to put args to the template renderer

print(outputText)