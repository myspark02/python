def foo10(a_list):
    a_list += [200, 300, 450]
    # a_list = a_list + [200, 300, 450] # this is slight different from the above

my_list = [1, 2, 3]
foo10(my_list)
print(my_list)


# def foo9(a_list) :
#     # a_list = [200, 300, 400]
#     a_list.append(4)
#     a_list[0] = -100

# my_list = [1, 2, 3]
# foo9(my_list)
# print(my_list)    

# def foo8(x) :
#     x = 5

# var = 10
# foo8(var)
# print(var)    


# def foo7() :
#     global number
#     x = number
#     number = 3
#     # number = 3 # make a variable number local variable
#     print('number inside function:', x)

# number = 0
# foo7()
# print(number)

# def foo6(a, b, c) :
#     print(a, b, c)

# my_list = [1, 2, 3]

# foo6(*my_list) #unpack argument, lenth of a list must match the number of parameter

# my_dict = {'a':1, 'b':2, 'c':3}
# foo6(**my_dict)


#
#  def foo5(*, last) :
#     print(last)

# foo5(last=200)    


# def foo4(*args, last) :
#     for arg in args :
#         print(arg)

#     print(last)
# foo4(1, 2, 3, 4, last=100)

# foo4(1, 2, 3) # error

# def foo3(a, b, *, c, d) : # after * there must come keyword arguments
#     print(a, b, c, d)
#     for arg in args :
#         print(arg)

# foo3(1, 4, c=3, d='hong')
# foo3(1, 2, 3, 4)

# def foo2(a, b, *args, **kwargs) :
#     print(a, b)
#     for arg in args :
#         print(arg)

#     for key in kwargs :
#         print(key, kwargs[key])    


# foo2(1, 2, 3, 4, 5, six=6, seven=7)

# foo2(1, 2, 4)

# foo2(1, 2, three=3)

# def foo(a, b, c, d=4) :
#     print(a, b, c, d)


# foo(1, 2, 3)    
# foo(1, 2, 3, 7)

# def print_name(name):
#     print(name)

# def fool(a, b, c) :
#     print(a, b, c)

# print_name('Alex')

# fool(1, 3, 3)
# fool(c=3, a=1, b=2)
# fool(1, c=2, b=5)

# fool(1, b=2, 4) # error. positional arguments cannot appear after keyword arguments
# fool(1, b=2, a=3) #error

