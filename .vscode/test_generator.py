import sys

mygenerator = (i for i in range(10000) if i%2==0)
# for i in mygenerator :
#     print(i)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10000) if i%2==0]   
# print(mylist)
print(sys.getsizeof(mylist))

# print(list(mygenerator))

# def fibonacci(limit) :
#     # 0 1 1 2 3 5 8 13 21 ...
#     a, b = 0, 1
#     while a < limit :
#         yield a
#         a, b = b, a+b
          

# fib = fibonacci(30)
# print(list(fib))
# for i in fib :
#     print(i)
# import sys

# def firstn(n) :
#     nums = []
#     num = 0
#     while num < n :
#         nums.append(num)
#         num += 1
#     return nums
# def firstn_generator(n) :
#     num = 0
#     while num < n :
#         yield num
#         num += 1

# print(firstn(10))  
# print(sum(firstn(10)))

# print(sum(firstn_generator(10)))
# print(sys.getsizeof(firstn(100000)))
# print(sys.getsizeof(firstn_generator(100000)))


# def countdown(num) :
#     print('Starting')
#     while num > 0 :
#         yield num
#         num -= 1

# cd = countdown(10)

# print(next(cd))
# print(next(cd))
# print(next(cd))



# def mygenerator() :
#     yield 3
#     yield 2
#     yield 1

# g = mygenerator()
# print(sum(g))
# print(sorted(g))
# print(g)
# for i in g :
#     print(i)
# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)