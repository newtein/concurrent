
threadCount=10
f=open("multithreading.txt","w")

import os
import time
#for thread in range(10,799,20):
for thread in range(300,800,2):
    os.system("py -3 pyrebasetest.py "+str(thread))
    time.sleep(10)
f.close()

print("Done!")
