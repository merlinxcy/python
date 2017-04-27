import time,threading
lock=threading.Lock()
balance=0
def change_it(n):
  global balance
  balance=balance+n
  balance=balance-n

def run_thread(n):
  for i in range(100000):
    lock.acquire()
    change_it(n)
    lock.release()

t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print balance
