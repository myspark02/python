
from time import time


# def myadd(func) :
#     def wrap(x, y=10) :
#         before = time()
#         rv = func(x, y)
#         after = time()
#         print("Elapsed:", after-before)
#         return rv
#     return wrap


def myadd(func) :
    def wrap(*args, **kwargs) :
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("Elapsed:", after-before)
        return rv
    return wrap

# n=2
# def ntimes(func) :
#     def wrapper(*args, **kwargs) :
#         for _ in range(n) :
#             print('running {.__name__}'.format(func))
#             rv = func(*args, **kwargs)
#         return rv
#     return wrapper


def ntimes(n) :
    def inner(func) :
        def wrapper(*args, **kwargs) :
            for _ in range(n) :
                print('running {.__name__}'.format(func))
                rv = func(*args, **kwargs)
            return rv
        return wrapper
    return inner    

def timer(func, x, y):
    before = time()
    rv = func(x, y)
    after = time()
    print("Elapsed:", after-before)
    return rv

# @ntimes
@myadd
def add(x, y=10) :
    return x+y

@ntimes(5)
def sub(x, y=10) :
    return x - y

# print(add(10, 20))

print(sub(40, 30))

# add = myadd(add)

# print(add(20, 50))

# timer(add, 10, 20)

# before = time()
# print('add(10)', add(10))
# after = time()
# print('add(20, 30)', add(20, 30))
# print('add("a", "b")', add("a", "b"))