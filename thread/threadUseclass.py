#!-*-coding:utf-8
#!-*-author:xeldax-*-
##创建thread实例，传给它一个可调用的类实例
import threading
from time import sleep,ctime

loops=[4,2]
class threadclass:
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args

    def __call__(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=threading.Thread(target=threadclass(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    for i in nloops:
        print i
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all done at:',ctime()

if __name__=='__main__':
     main()
