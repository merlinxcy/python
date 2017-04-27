#-*-encoding:utf-8-*-#
import socket
import argparse
import threading
lock =threading.Lock()
threads=[]
port=[]
parser=argparse.ArgumentParser()
parser.add_argument("-ip",action='store',dest='ip',type=str,help='Specify the ip address!')
args=parser.parse_args()
opennum=0
def portScanner(ip,port):
  global opennum
  try:
    s=socket.socket()
    #print '[*] Attemping to connect to'+ip+':'+str(port)+'\n'
    s.connect((ip,port))
    print '[*] Port'+str(port)+'open \n'
    opennum+=1
    port.append(port)
  except:
    #print '[*] Port'+str(port)+'is close \n'
    pass
  finally:
    s.close()

def main():
  for p in range(0,1000):
    t=threading.Thread(target=portScanner,args=(args.ip,port))
    threads.append(t)
    t.start()
  for t in threads:
    t.join()
  print '[+]Scanning over.'+str(opennum)+'numbers\' ports is opened\n'
  print '[+]Open port:'
  print str(port)

if __name__=='__main__':
  main()
