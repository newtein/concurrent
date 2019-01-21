
'''
#firebase retrivel
from firebase import firebase
import timecalc as t
firebase=firebase.FirebaseApplication('https://trail-ceb25.firebaseio.com/')
@t.timeit
def pyre():
    
   
        for i in range(0,200):
             
             firebase.get("5555555"+str(30),None)
       

for j in range(2):
    pyre()

'''


#firebase insertion
'''
from firebase import firebase
import timecalc as t
firebase=firebase.FirebaseApplication('https://trail-ceb25.firebaseio.com/')
@t.timeit
def pyre():
    
   
        for i in range(0,200):
             firebase.post("5555555"+str(i)+"/"+"create",{"filename":"100"})
       

for j in range(2):
    pyre()
'''
'''
#pyrebase insertion
import pyrebase
import timecalc as t
config = {
        "apiKey": "AIzaSyDcy7IT1XY6GCdAv3ZvBuG4oeOV7hsMEFI",
        "authDomain": "trail-ceb25.firebaseapp.com",
        "databaseURL": "https://trail-ceb25.firebaseio.com",
        "projectId": "trail-ceb25",
        "storageBucket": "trail-ceb25.appspot.com",
        "messagingSenderId": "421329178141"
    }

firebase = pyrebase.initialize_app(config)

@t.timeit
def pyre():
    
        db = firebase.database()
        for i in range(0,200):
             db.child("5555555"+str(i)).child("create"+str(i)).push({"filename":"100"})
             #db.child("5555555"+str(i)).child("create"+str(i)).get().val()
       

for j in range(2):
    pyre() 
'''


#pyrebase retrival
import pyrebase
import timecalc as t
import sys,os,re
IS_PY2 = sys.version_info < (3, 0)

if IS_PY2:
    from Queue import Queue
else:
    from queue import Queue

from threading import Thread
config = {
        "apiKey": "AIzaSyDcy7IT1XY6GCdAv3ZvBuG4oeOV7hsMEFI",
        "authDomain": "trail-ceb25.firebaseapp.com",
        "databaseURL": "https://trail-ceb25.firebaseio.com",
        "projectId": "trail-ceb25",
        "storageBucket": "trail-ceb25.appspot.com",
        "messagingSenderId": "421329178141"
    }

firebase = pyrebase.initialize_app(config)

class Worker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()
       


class ThreadPool:
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, args_list, **kargs):
        """ Add a task to the queue """
       
        self.tasks.put((func, args_list, kargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """ Wait for completion of all the tasks in the queue """
        self.tasks.join()


def pyrefire(clcp):
            db = firebase.database()
              
            #f=db.child("5555555"+str(clcp%49)).child("create"+str(40)).get().val()v 
            # db.child("5555555"+str(clcp%49)).child("create"+str(40)).push({"filename":"100"})
            db.push("5555555"+str(clcp)[0])
            
            #print(f)
                  
                                              

@t.timeit
def pyre(thread):  
        pool=ThreadPool(thread)
        #db = firebase.database()
        print(thread)
        for i in range(0,50000):
                pool.add_task(pyrefire,[i])
        print("Queries="+str(i))
        


import sys
import time
import pickle


thread=int(sys.argv[1])
#fw=open("upload"+str(thread)+".txt","a")
pyre(thread)
