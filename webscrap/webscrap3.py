#-*-coding:utf-8-*-#
import urllib2
def downloading(url):
  print('Downloading:',url)
  try:
      html=urllib2.urlopen(url).read()
  except urllib2.URLError as e:
      print('Download error:',e.reason)
      html=None
      if num_retries
  return html
URL=input('url:')
downloading(URL)