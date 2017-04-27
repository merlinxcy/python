import socket
import threading
import time
host="0.0.0.0"
port=12345
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)

'''
def server_handle(server_sock):
  reply=server_sock.recv(1024)
  while True:
    print reply+"\n"
    time.sleep(0.5)
    if reply=="Bye":
      server_sock.send("Bye")
      server_sock.close()
      break
    elif reply=="hello":
      server_sock.send("hello")
    reply=server_sock.recv(1024)
'''
def server_handle(server_sock):
  while True:
    reply=server_sock.recv(1024)
    if reply:
      print reply
    server_sock.send("hello")

while True:
  sock,addr=server.accept()
  th=threading.Thread(target=server_handle,args=(sock,))
  th.start()
  
