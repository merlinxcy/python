import subprocess
print('$ nslook www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('exit code:',r)

