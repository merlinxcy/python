import urllib2
import random
import time
import re
"""
index=[i+1 for i in range(50)]
for pa in index:
  try:
    if pa==1:
      url="http://cq.fang.lianjia.com/loupan/"
    else:
      url="http://cq.lianjia.com/loupan/pg%d/"%(pa)
      print "request: "+url
      time.sleep(3)
      req=urllib2.Request(url)
      data=urllib2.urlopen(req)
      #html=open("html111111.html","w")
      #html.write(data)
      #html.close()
      res=data.read()
      html=open("html111111.html","w")
      html.write(res)
      html.close()
      print res
      groups = re.findall(r'"rateContent":"(.*?)","rateDate"',ws1)
      break
  except Exception as e:
    print e
    break
"""
#-*-coding:utf-8-*-#
import pandas as pd
url="http://jn.fang.lianjia.com/loupan/"
data=urllib2.urlopen(urllib2.Request(url)).read()
html=open("html111111.html","w")
html.write(data)
html.close()
g=re.findall('<span class="text">(.*?)</span>',data)
a=g[0].decode('utf-8')
print a
#pf=pd.DataFrame=({"content": g})
#pf.to_csv('file1.csv', index=False)
ans=open("ans.txt","w")
ans.write(str(g))
ans.close()
print g
