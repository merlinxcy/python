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
    print "NET TOOL"
    print
    print "Usage:netcat.py -t target_host -p port"
    print "-l --listen"
    print "-e --execute=file_to_run"
    print "-c --command:
    print "-u --upload=destination
