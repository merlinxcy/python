file=open("/root/temp","r")
passwd=list()
while True:
  line=file.readline()
  if not line:
    break
  passwd.append(line[:-1])
print passwd
  
