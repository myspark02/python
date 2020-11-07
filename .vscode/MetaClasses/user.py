#user.py
from library import Base

# assert hasattr(Base, 'foo'),  "You broke it, you fool!"

class Derived(Base) :
    def bar(self) :
        return self.foo()

# class Derived :
#     def bar(self) :
#         return 'bar'

d = Derived()
d.bar()