

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename) :
    f = open(filename, 'w')
    try :
        yield f
    finally :
        f.close()

with open_mangaged_file('notes.txt') as f :
    f.write('some todo.....')

    
# from threading import Lock

# class ManagedFile :
#     def __init__(self, filename) -> None:
#         self.filename = filename
#         print('init')

#     def __enter__(self) :
#         print('enter')
#         self.file = open(self.filename, 'w')
#         return self.file       

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if self.file :
#             self.file.close()
#         if exc_type is not None :
#             print('exception has been handled')
#         # print('exc:', exc_type, exc_value)
#         print('exit')
#         return True # manually handle exception and make no exception raise cause this method already handled it

# with ManagedFile('notes.txt') as file :
#     print('do some stuff')
#     file.write('some todo...')
#     file.somemethod()
# print('continuing')

# lock = Lock()
# lock.acquire()

# lock.release()

# with lock :
#     # ...
    
# with open('notes.txt', 'w') as file :
#     file.write('some todo ...')

# file = open('notes.txt', 'a')
# try :
#     file.write('something todo...')
# except:  
#     print("error")
# finally :
#     file.close