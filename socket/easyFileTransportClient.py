import socket
import threading
import os
import sys
import getopt
import tkinter as tk
host="0.0.0.0"
port=12345
listen_flag=0
GUI_flag=0
filepath="/root/File/Programe/Python/socket/program"


def get_info():
  global listen_flag
  global GUI_flag
  try:
    options,args=getopt.getopt(sys.argv[1:],"t:p:l:G:f:",\
      ["target","port","listen","GUI","filepath"])
  except getopt.GetoptError as err:
    print str(err)
    print "Usage:[target][port][listen][GUI][filepath]"
  for op,a in options:
    if op in("-t","--target"):
      host=a
    elif op in("-p","--port"):
      port=a
    elif op in("-l","--listen"):
      listen_flag=1
    elif op in("-G","--GUI"):
      GUI_flag=1
    elif op in("-f","--filepath"):
      filepath=a
    else:
      assert False,"Unhandled Option"


def readfile_handle(location):
  file=open(location,"rb")
  buf=file.read()
  file.close()
  return buf

def savefile_handle(location,buf):
  file=open(location,"wb")
  try:
    file.write(buf)
  except:
    print "[-]Savefile_handle Error occured!"
  finally:
    file.close()

def client_handle():
  client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.connect((host,port))
  buf=readfile_handle(filepath)
  client.send(buf)
  reply=client.recv(1024)
    
#  while True:
#   temp=client.recv(1024)
#   print len(temp)
#   if len(temp)<1024:
#    break
#   else:
#    reply=reply+temp
  
  print "[*] Recevied:  %s" % reply
  client.close()


def server_startup():
  global host
  global port
  server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server.bind((host,port))
  server.listen(5)
  print "[*]Server start--->  IP:%s Port: %s" % (host,port)
  return server

def server_handle(server_sock):
  server_sock.send(b'ACK')
  reply=server_sock.recv(1024)
  while True:
    temp=server_sock.recv(1024)
    if len(temp)<1024:
      break
    else:
      reply=reply+temp
  #server_sock.send(b'ACK')
  print "[*] Recevied:  %s" % reply
  savefile_handle("/root/download/fileSave",reply)
  server_sock.close()

def server_loop():
  server=server_startup()
  while True:
   server_sock,addr=server.accept()
   server_to_clienthandle=threading.Thread(target=server_handle,args=(server_sock,))
   server_to_clienthandle.start()

def confirm():
  global host
  root=tk.Tk()
  #host=tk.StringVar()#bug
  host=str(host.get())#bug
  print host
  client_handle()
'''
if __name__=='__main__':
  get_info()
  a=input("Server[1] or Client[2]\n")
  #print a
  if a==2:
    client_handle()
    exit()
  if a==1:
    server_loop()
'''
def GUI():
  global host
  root=tk.Tk()
  host=tk.StringVar()
  labelframe=tk.Frame(root)
  infoframe=tk.LabelFrame(root,padx=10,pady=10)
  labelframe.grid()
  infoframe.grid(padx=30,pady=30)

  label_title=tk.Label(labelframe,text="Simple    ftp    script")
  label_target=tk.Label(infoframe,text="Target ip")
  entry_target=tk.Entry(infoframe,textvariable=host)
  label_filepath=tk.Label(infoframe,text="File Path")
  entry_filepath=tk.Entry(infoframe)
  button_confirm=tk.Button(infoframe,text="Confirm",command=confirm)
  button_exit=tk.Button(infoframe,text="Exit",command=lambda:sys.exit(0))
  label_title.grid()
  label_target.grid(row=0,column=0,sticky=tk.W)
  entry_target.grid(row=0,column=1,sticky=tk.W)
  label_filepath.grid(row=2,column=0,sticky=tk.W)
  entry_filepath.grid(row=2,column=1,sticky=tk.W)
  button_confirm.grid(row=4,column=0,sticky=tk.W)
  button_exit.grid(row=4,column=1,sticky=tk.E)
  root.mainloop()

def consoleline():
  if listen_flag==1:
    server_loop();
  if listen_flag==0:
    client_handle()




if __name__=='__main__':
  get_info()
  if GUI_flag==1:
    print "GUI mode only support client mode"
    GUI()
  else:
    consoleline()









  
