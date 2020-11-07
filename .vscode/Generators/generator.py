# top-level syntax, function -> underscore methods    
# x()       __call__

from time import sleep

# def add1(x, y) :
#     return x+y

# class Adder :
#     # def __init__(self) :
#     #     self.z = 0
#     def __call__(self, x, y) :
#         return x + y

# add2 = Adder()

# print(add2(3, 5))

# def generateFromOneToHundred() :
#     for i in range(1, 101) :
#         yield i

# for i in generateFromOneToHundred() :
#     print(i)

# def compute() :
#     rv = []
#     for i in range(10) :
#         sleep(.5)
#         rv.append(i)
#     return rv


# for i in compute() :
#     print(i)

# class Compute:
    # def __call__(self) :
    #     rv = []
    #     for i in range(10) :
    #         sleep(.5)
    #         rv.append(i)
    #     return rv

    # def __iter__(self) :
    #     self.last = 0
    #     return self

    # def __next__(self) :
    #     rv = self.last
    #     self.last += 1
    #     if self.last > 10:
    #         raise StopIteration()
    #     sleep(.5)
    #     return rv


# compute = Compute()

# for i in compute :
#     print(i)

def generator() :
    for i in range(10) :
        sleep(.5)
        yield i

for i in generator() :
    print(i)
# for x in xs:
    # pass

# xi = iter(xs)    -> __iter__
# while True :
#     x = next(xi)  -> __next__

# class Api :
#     def run_this_first(self) :
#         first()
    
#     def run_this_second(self) :
#         second()

#     def run_this_last(self) :
#         last()


# def api() :
#     first()
#     yield
#     second()
#     yield
#     last()

