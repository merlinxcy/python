#-*-coding:utf-8-*-#
import logging

logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',filename='./fireOS.log',level=logging.INFO)

def check_string(s):
  if not s:
    return False
  if isinstance(s,str) or isinstance(s,unicode):
   #ininstace函数用来判别数据类型，类似type函数
    return True
  return False


def display(s):
  if check_string(s):
   logging.info(s)
   print s

def logit(s):
  if check_string(s):
   logging.info(s)
