import requests
import re
import time
headers={'User-Agent':'as'}
r=requests.get('http://www.xicidaili.com/wt',headers=headers)
page=r.content
maxpage=re.findall(r'<a href="/wt/.*?">(.*?)</a>',page)
#print maxpage.sort()
maxpage=max(int(i) for i in maxpage)
#print page
#page="<td>1.1.1.11</td>sdsd<td>10.0.0.3</td>"
#result=re.findall(r'<td>([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})</td>.*?<td>(.*?)</td>',page)    ????????????
result=re.findall(r'<td>(.*?)</td>',page)
proxylist=list()
for i in range(0,len(result)/5):
    ip=result[i*5]
    port=result[i*5+1]
    proxylist.append({ip:port})
print proxylist
print '11111111111'
#print proxylist
#print result
if maxpage>1:
    for i in range(2,10):
        url='http://www.xicidaili.com/wt/'+str(i)
        #time.sleep(2)
        #print url
        r=requests.get(url,headers=headers)
        page=r.content
        #print page
        result=re.findall(r'<td>(.*?)</td>',page)
        for i in range(0,len(result)/5):
            ip=result[i*5]
            port=result[i*5+1]
            proxylist.append({ip:port})
print proxylist
