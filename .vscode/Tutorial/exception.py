#Errors and Exceptions
# import somemodudle

class ValueTooHighError(Exception) :
    pass

class ValueTooSmallError(Exception) :
    def __init__(self, message, value) :
        self.message = message
        self.value = value


def test_value(x) :
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)
try :    
    test_value(1)    
except ValueTooHighError as e :
    print(e)    
except ValueTooSmallError as e :
    print(e.message, e.value)    

# try :
#     a = 5/1
#     b = a+ 4
    # print('you can\'t see this line')
# except Exception as e:
# except ZeroDivisionError as e:
#     # print('an error happend')
#     print(e)
# except TypeError as e:
#     print(e)    
# else :
#     print('everything is fine')    
# finally :
#     print("cleaning up...")    


# x = 5
# assert(x >= 0), 'x is not positive'
# x = -5;
# if x < 0:
#     raise Exception('x should be positive')
# my_dict = {'name':'Max'}
# my_dict['age']

# a = [1, 2, 3]
# a.remove(4)

# print(a)

# f = open('somefile.txt')

# a=5
# b=c

# a = 5 + '10'