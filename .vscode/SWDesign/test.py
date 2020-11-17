# import MathFunctions

# print(MathFunctions.get_average([1, 4, 5, 7, 8, 9]))

# ht = {"key1":100, "key2":150, "key3": 98}
# print(MathFunctions.max_value(ht))


# from HashTableFunctions import get_max as get_ht_max, get_min as get_ht_min
# from ListMathFunctions import get_max, get_min
# import HashTableFunctions as h

# ht = {"key1":100, "key2":150, "key3": 98}
# print(h.get_max(ht))
# print(get_ht_min(ht))
# print(h.get_keys(ht))
# # print(get_max([1, 2, 3, 4, 5, 7]))

# Package : A Folder full of python files..., and touch a file named __init__.py then this folder becomes a package
from util import HashTableFunctions as h, ListMathFunctions as l

ht = {"key1":100, "key2":150, "key3": 98}
print(h.get_keys(ht))
print(l.get_max([1, 3, 5, 9]))