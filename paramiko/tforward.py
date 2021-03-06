import paramiko


def main():
    options,server,remote = parse_options()
    password = None
    if options.readpass:
        password = getpass.getpass('Enter ssh password')
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    verbose('Connecting to ssh host')
    try:
        client.connect(server[0], server[1], username=options.user, key_filename=optoins.key_file
                       ,look_for_keys=options.look_for_key, password=password)
    except Exception as e:
        sys.exit(1)
    verbose('s')
    try:
        reverse_forward_tunnel(options.port, remote[0], remote[1], client.get_transport())
    except KeyboardInterrupt:
        sys.exit(0)

def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
    transport.request_port_forward('', server_port)
    while True:
        chan = transport.accept(1000)
        if chan is None:
            continue
        thr = threading.Thread(target=handler, args(chan,remote_host,remote_port))
        thr.setDaemon(True)
        thr.start()

def handler(chan,host,port):
    sock = socket.socket()
    try:
        sock.connect((host,port))
    except Exception as e:
        verbose()
        return
    while True:
        r,w,x = select.select([sock,chan],[],[])
        if sock in r:
            data = sock.recv(1024)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.recv(1024)
            if len(data) == 0:
                break
            sock.send(data)
        chan.close()
        sock.close()
        verbose()
