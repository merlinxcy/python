'''
from progressbar import ProgressBar
import time
pbar=ProgressBar(maxval=10)
for i in pbar(range(100)):
    time.sleep(0.02)
pbar.finish()
'''
'''
import progressbar
import time
bar=progressbar.ProgressBar(10)
for i in bar(range(10)):
    #print i
    time.sleep(0.2)
    bar.update(i)
'''
