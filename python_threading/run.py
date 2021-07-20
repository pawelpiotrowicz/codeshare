import logging
import threading
import time
import os



import ctypes
libc = ctypes.cdll.LoadLibrary('libc.so.6')
# System dependent, see e.g. /usr/include/x86_64-linux-gnu/asm/unistd_64.h
SYS_gettid = 186

def getLinuxThreadId():
   """Returns OS thread id - Specific to Linux"""
   return libc.syscall(SYS_gettid)



def thread_function(name):
    _pid = os.getpid()
    logging.info("LogicThreadId %s: starting  os.getpid(%d) getLinuxThreadId(%d) threading.get_ident(%x) threading.get_native_id(%d)", name, os.getpid(), getLinuxThreadId(), threading.get_ident(),threading.get_native_id())
    time.sleep(100)
    logging.info("Thread %s: finishing", name)



if __name__ == "__main__":
    # format = "%(asctime)s: %(message)s"
    format = "[%(asctime)s %(threadName)s ]:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    threads = []
    
    for num in range(1,3):
       # x = threading.Thread(target=thread_function, args=(num,),daemon=True)
       x = threading.Thread(target=thread_function, args=(num,))
       threads.append(x)
     

    logging.info("Main    : before running thread")

    for x in threads:
       x.start()

    logging.info("Main    : wait for the thread to finish")

    for x in threads:
        x.join()

    logging.info("Main    : all done")