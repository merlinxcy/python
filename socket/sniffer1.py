#-*-coding:utf-8-*-#
import socket
import os
#host to listen on
host="192.168.237.129"
if os.name=="nt":
   socket_protocol=socket.IPPROTO_IP
else:
   socket_protocol=socket.IPPROTO_ICMP
sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
sniffer.bind((host,0))
if os.name=="nt":
   sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
print sniffer.recvfrom(65565)
if os.name=="nt":
   sniffer.iotcl(socket.SIO_RCVALL,socket.RCVALL_OFF)
