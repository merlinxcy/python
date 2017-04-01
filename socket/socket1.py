import socket
host_name="192.168.237.111"
host_port=1234
#create socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host_name,host_port))
client.send("Cisco 514 UDP Flood Denial of Service Vulnerability")
response=client.recv(4096)
print	response
