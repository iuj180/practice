import subprocess

ip_addresses = ['172.31.164.1', '172.31.164.3', '172.164.5']

for ip_address in ip_addresses:
    command = f'mstsc /v:{ip_address}'
    subprocess.call(command, shell=True)