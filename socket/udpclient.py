import socket
import time
target_name="192.168.137.111"
target_port=137
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
  client.sendto("AA",(target_name,target_port))
  time.sleep(1)
  print('aaa')
data,addr=client.recvfrom(4096)
print data
