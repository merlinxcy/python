import multiprocessing
import os
def run(name):
  print "run child process %s(%s)"%(name,os.getpid())

if __name__=='__main__':
  print "parent process %s."%os.getpid()
  p=multiprocessing.Process(target=run,args=('test',))
  p.start()
  p.join()
  print 'child process end'

