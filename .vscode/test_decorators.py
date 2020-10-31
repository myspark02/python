import functools

def start_end_decorator(func) :
    # def wrapper() :
    @functools.wraps(func)
    def wrapper(*args, **kwargs) :
        print('Start')
        # func()
        # func(*args, **kwargs)
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper        

@start_end_decorator  #do the same thing as below, i.e, print_name = start_end_decorator(print_name)
# def print_name() :
#     print('scpark')
def add5(x) :
    return x + 5

# print_name = start_end_decorator(print_name)
# add5(10)
result = add5(10)
print(result)
# print(help(add5))
print(add5.__name__)
