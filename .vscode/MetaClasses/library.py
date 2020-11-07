#library.py

class BaseMeta(type) :
    def __new__(cls, name, base, body):
        print('BaseMeta.__new__', ',cls:', cls, ',name:', name, ',base:', base, ',body:', body)
        if name=='Derived' and  not 'bar' in body :
            raise TypeError("bad user class")
        return super().__new__(cls, name, base, body)



class Base(metaclass=BaseMeta) :
    def foo(self) :
       print("foo")

    def __init_subclass__(self, *a, **kw) :
        print('init_subclass', a, kw)
        return super().__init_subclass__(*a, **kw)



# class Base :
#     def foo(self) :
#         return 'foo'

# import builtins


# class Base :
#     def foo(self) :
#         return self.bar()


# Everything is executable in python like followings
# for _ in range(10) :
#     class Base : pass

# class Base :
#     for _ in range(10) :
#         def bar(self) :
#             pass

# def _() :
#     class Base :
#         pass

# from dis import dis

# dis(_)

# old_bc = __build_class__
# def my_bc(*a, **kw) :
#     print('my buildclass->', a, kw)
#     return old_bc(*a, **kw)

# def my_bc(func, name, base=None, **kw) :
#     if base is Base :
#         print('check if bar method defined')
#     if base is not None:    
#         return old_bc(func, name, base, **kw)
#     else :
#         return old_bc(func, name, **kw)

# import builtins
# builtins.__build_class__ = my_bc

