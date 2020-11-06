from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue

import time

def square_numbers() :
    for i in range(1000):
        i * i

def add_100(number, lock) :
    for i in range(100) :
        time.sleep(0.01)
        with lock:
            number.value += 1
        # lock.acquire()
        # number.value += 1
        # lock.release()

def add_100_array(array, lock) :
    for i in range(100) :
        time.sleep(0.01)
        for j in range(len(array)) :
            with lock :
                array[j] += 1

def square(numbers, queue) :
    for i in numbers :
        queue.put(i*i)

def make_negative(numbers, queue) :
    for i in numbers :
        queue.put(-1*i)

def cube(number) :
    return number*number*number


if __name__ == '__main__' : 
    numbers = range(10)
    print(numbers)
    pool = Pool()
# map, apply, join, close
    # result = pool.map(cube, numbers)
    result = pool.map(cube, [4, 5, 6])
    # pool.apply(cube, numbers[2])
    pool.close()
    pool.join()

    print(result)

#     q = Queue()

#     numbers = range(1, 6)

#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty() :
#         print(q.get())





    # lock = Lock()

    # shared_array = Array('d', [0.0, 100.0, 200.0])
    # print('array at beginning is ' , shared_array[:])

    # p1 = Process(target=add_100_array, args=(shared_array, lock))
    # p2 = Process(target=add_100_array, args=(shared_array, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print('array at end is ' , shared_array[:])


    # shared_number = Value('i', 0)
    # print('Number at beginning is ', shared_number.value)

    # lock = Lock()

    # p1 = Process(target=add_100, args=(shared_number,lock))
    # p2 = Process(target=add_100, args=(shared_number,lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print('number at end is ', shared_number.value)
