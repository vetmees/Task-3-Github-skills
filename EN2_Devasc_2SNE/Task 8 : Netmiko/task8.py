from netmiko import ConnectHandler

SW01 = {
'device_type': 'cisco_ios',
'host':   '192.168.10.164',
'username': 'admin',
'password': 'cisco',
'port' : 22  
}

net_connect = ConnectHandler(**SW01)

config_commands = [
     'do show version' , ' int GigabitEthernet0/1', 'description 0.0.0.4 255.255.255.0', 'no shut', 'do show run'
]
net_connect.enable()
output=net_connect.send_config_set(config_commands)

print(output)
