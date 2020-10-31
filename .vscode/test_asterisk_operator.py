
dict_a = {'a': 1, 'b':2}
dict_b = {'c':3, 'd':4}

my_dict = {**dict_a, **dict_b }
print(my_dict)

# my_tuple = (1, 2, 3)
# my_list = [4, 5,6]
# my_set = {7, 8, 9}
# new_list = [*my_tuple, *my_list, *my_set]
# print(new_list)
# numbers=(1,2,3,4,5,6,7)

# # *beginning, last = numbers
# beginning, *middle, secondlast, last = numbers
# print(beginning)
# print(middle)
# print(secondlast)
# print(last) 


# numbers = [1, 2, 3, 4, 5, 6]
# *beginning, last = numbers
# print(beginning)
# print(last)
# # def foo3(a, b, c) :
#     print(a, b, c)

# my_list = [1, 2, 3]
# foo3(*my_list)

# my_dict = {'a': 5, 'b':6, 'c':7}
# foo3(**my_dict)
# def foo2(a, b, *, c) :
#     print(a, b, c)

# # foo2(1, 2, 3)
# foo2(1, 2, c=3)

# def foo(a, b, *args, **kwargs) :
#     print(a, b)
#     for arg in args :
#         print(arg)
#     for key in kwargs :
#         print(key, kwargs[key])

# foo(1, 2, 3, 4, 5, six=6, seven=7)

# result = 5*7
# result = 2**4

# zeros = [0] * 10
# zeros = [0,1]*10
# zeros = (0,1)*10
# zeros = "AB"*10
# print(zeros)
# print(result)