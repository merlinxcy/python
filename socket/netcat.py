#Version one beta
#made by xeldax
import sys
import socket
import getopt
import threading
import subprocess
listen=False
command=False
upload=""
execute=""
target=""
upload_destination=""
port=0
def usage():
    print "net tool"
    print
    print "Usage:netcat.py -t target_host -p port"
    print "-l --listen"
    print "-e --execute=file_to_run"
    print "-c --command"
    print "-u --upload=destination"
    print
    print "Examples:"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -c"
    print r"netcat.py -t 192.168.0.1 -p 5555 -u=c:\target.exe"
    print "netcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./netcat.py -t 192.168.0.1 -p 135"
    print 
    sys.exit(0)
#client_sender
def client_sender(buffer):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        #connect to our target host
        client.connect((target,port))
        if len(buffer):
          client.send(buffer)
        while True:
          recv_len=1
          response=""
          while recv_len:
              data=client.recv(4096)
              recv_len=len(data)
              response+=data
              if recv_len<4096:
                 break
          print response,
          buffer=raw_input("")
          buffer+="\n"
          client.send(buffer)
    except:
        print "[*] Exception! Exiting."
        client.close()

def server_loop():
    global target
    if not len(target):
        target="0.0.0.0"
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)
    while True:
        client_socket,addr=server.accept()
        client_thread=threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()

def run_command(command):
    command=command.rstrip()
    try:
        output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output="Failed to execute command.\r\n"
    return output

def client_handler(client_socket):
    global upload
    global execute
    global command
    if len(upload_destination):
       file_buffer=""
       while True:
          data=client_socket.recv(1024)
          if not data:
              break
          else:
              file_buffer+=data
       try:
           file_descriptor=open(upload_destination,"wb")
           file_descriptor=write(file_buffer)
           file_descriptor.close()
           client_socket.send("Successfully saced file to %s\r\n" % upload_destination)
       except:
           client_socket.send("Failed to sace file")
    if len(execute):
        output=run_command(execute)
        client_socket.send(output)
    if command:
        while True:
          client_socket.send("<BHP:#> ")
          cmd_buffer=""
          while "\n" not in cmd_buffer:
              cmd_buffer+=client_socket.recv(1024)
          response=run_command(cmd_buffer)
          client_socket.send(response)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destinantion
    global target
    if not len(sys.argv[1:]):
        usage()
    #read the commandline options
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu:",\
        ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in("-h","--help"):
           usage()
        elif o in ("-l","--listen"):
           listen=True
        elif o in ("-e","--execute"):
           execute=True
        elif o in ("-c","--commandshell"):
           command=True
        elif o in ("-u","--upload"):
           upload_destination=a
        elif o in ("-t","--target"):
           target=a
        elif o in ("-p","--port"):
           port=int(a)
        else:
           assert False,"Unhandled Option"
    if not listen and len(target) and port>0:
        #use ctrl-d to interrupt
        buffer=sys.stdin.read()
        #send data
        client_sender(buffer)
        #main fun gooooo
    if listen:
           server_loop()


#main
if __name__=='__main__':
  print sys.argv  
  main()
  


















