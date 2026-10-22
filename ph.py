import netmiko
from netmiko import ConnectHandler
import json
# import pprint as print

with open('ph.json', 'r') as jfile:
    pfile = json.load(jfile)
    print(pfile)


jp = {
    'device_type': 'cisco_ios',
    'host': '192.168.102.12',
    'username': 'admin',
    'password': 'pass',
    'port': 22,
    'secret': 'pass'
}


config = [
    f'interface {pfile["type"]} {pfile["id"]}',
    f'ip add {pfile["ipv4"]["ip"]} {pfile["ipv4"]["mask"]}',
    f'description {pfile["desc"]}',
    'end'
]



cli = ConnectHandler(**jp)
cli.enable()
cli.send_config_set(config)
siib = cli.send_command('show ip int br')
cli.disconnect()
print(siib)