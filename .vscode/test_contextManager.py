

from threading import Lock

lock = Lock()

lock.acquire()

lock.release()
# with open('notes.txt', 'w') as file :
#     file.write('some todo ...')

# file = open('notes.txt', 'a')
# try :
#     file.write('something todo...')
# except:  
#     print("error")
# finally :
#     file.close