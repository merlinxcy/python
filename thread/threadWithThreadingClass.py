#!-*-coding:utf-8
#!-*-author:xeldax-*-
##创建thread实例，传给它一个可调用的类实例
import threading
lock=threading.Lock()
class mythread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
    def run(self):
        lock.acquire()
        self.func(*self.args)
        lock.release()

def loop(p1,p2):
    print p1,p2
loops=[1,2,3]
def main():
    print loops
    threads=[]
    for i in range(0,len(loops)):
        t=mythread(loop,('ss:',i))
        threads.append(t)

    print '...'
    print threads
    for i in range(0,len(loops)):
        threads[i].start()

    for i in range(0,len(loops)):
        threads[i].join()

if __name__=='__main__':
    main()
