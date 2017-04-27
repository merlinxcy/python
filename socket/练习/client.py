import socket
import time
host="0.0.0.0"
port=12345
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send("ACK")
reply=client.recv(1024)
'''
while True:
  print reply+"\n"
  if reply=="ACK":
    client.send("hello")
    reply=client.recv(1024)
  elif reply=="Bye":
    client.send("Bye")
    client.close()
'''
while True:
  time.sleep(1)
  if reply:
    print reply
  client.send("ack")
  client.recv(1024)
