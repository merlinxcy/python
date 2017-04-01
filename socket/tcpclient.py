import socket
host_name="0.0.0.0"
host_port=1234
#create socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host_name,host_port))
client.send("Hello!")
response=client.recv(4096)
print	response
