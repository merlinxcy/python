from SocketServer import TCPServer,StreamRequestHandler
from time import ctime

host=''
port=21567
addr=(host,port)

class  MyRequestHandler(StreamRequestHandler):
	def handle(self):
		print "...connected from:",self.client_address
		self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))


tcpServ=TCPServer(addr,MyRequestHandler)
print "waiting for connection..."
tcpServ.serve_forever()