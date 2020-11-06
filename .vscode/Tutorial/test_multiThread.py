from multiprocessing import Process
import os
from os import lockf
import time

from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock) :
    while True:
        value = q.get() # block util item is availiable

        # processing
        with lock: # queue is thread-safe, then why is this lock necessary?
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == '__main__' :
    q = Queue()
    num_threads = 10
    lock = Lock()
    for i in range(num_threads) :
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # A daemon thread dies when main thread die
        thread.start()
    
    for i in range(1, 21) :
        q.put(i)

    q.join() # wait until all the items to be processed


    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3 2 1 -->
    # first = q.get() # remove and return an item from the Queue
    # print(first) 

    # q.task_done()
    # q.join()

    print('end_main')





# database_value = 0

# def increase(lock) :
#     global database_value
#     with lock:
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy

    # lock.acquire()
    # local_copy = database_value

    # # processing
    # local_copy += 1
    # time.sleep(0.1)
    # database_value = local_copy
    # lock.release()

# if __name__ == '__main__' :
#     lock = Lock()

#     print('start_value', database_value)

#     thread1 = Thread(target=increase, args=(lock, ))
#     thread2 = Thread(target=increase, args =(lock, ))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print('end value', database_value)

#     print('end_main')





# def square_numbers() :
#     for i in range(100) :
#         i * i 
#         time.sleep(0.1)

# threads = []
# num_threads = 10

# # create threads
# for i in range(num_threads) :
#     t = Thread(target=square_numbers)
#     threads.append(t)

# #start
# for t in threads:
#     t.start()

# # join
# for t in threads :
#     t.join()

# print('end_main')




# if __name__ == '__main__' :
#     processes = []
#     num_processes = os.cpu_count()
#     print('num_process : ' + str(num_processes))
#     #create processes

#     for i in range(num_processes) :
#         p = Process(target=square_numbers)
#         processes.append(p)

#     # start
#     for p in processes :
#         p.start()

#     #join
#     for p in processes :
#         p.join()

#     print('end main')