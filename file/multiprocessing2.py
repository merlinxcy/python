from multiprocessing import Pool
import os,time,random

def long_time_task(name):
  print "run task %s (%s)..." % (name,os.getpid())
  start=time.time()
  time.sleep(random.random()*3)
  end=time.time()
  print "task %s runs %0.2f seconds." % (name,(end-start))

if __name__=='__main__':
  print
