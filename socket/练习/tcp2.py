import socket
tcpclient=socket.socket(AF_INET,SOCK_STREAM)
tcpclient.getservbyname('http','tcp')
tcpclient.
