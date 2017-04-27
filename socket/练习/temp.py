import sys
import socket
if(len(sys.argv)<2):
  print "[-]ip and port is no specifyed"
  exit(0)
host=sys.argv[1]
port=sys.argv[2]
port=int(port)
print "[+]host:port is %s:%d is connecting"%(host,port)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
 client.connect((host,port))
except Exception as e:
 print "[-]error occur:%s"%e


client.send("hhhh")
while True:
 ans=client.recv(1024)
 if not len(ans):
  break
 print ans
