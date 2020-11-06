# Sets : unordered, ordered, no duplicates
# myset = {1, 2, 3, 1, 2}
# myset = set("Hello")
# print(myset)
# myset = {}
myset = set()   
# print(type(myset))
# myset.add(1)
# myset.add(2)
# myset.add(3)
# print(myset)
# myset.remove(3)
# print(myset)
# myset.discard(2)
# print(myset)
# myset.clear()
# print(myset)
# myset.add(1)
# myset.add(2)
# myset.add(3)
# print(myset.pop())
# print(myset.pop())
# print(myset)

# for i in myset:
#     print(i)

# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds .union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)

# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}
# diff = setA.difference(setB)
# print(diff)
# diff = setB.symmetric_difference(setA)
# print(diff)

# setA.update(setB)
# print(setA)

# setA={1, 2, 3, 4, 5}
# setB={1, 2, 3}
# setC={7, 8}
# print(setA.issubset(setB))
# print(setA.isdisjoint(setB))
# print(setA.isdisjoint(setC))

# setA = {1,2,3,4,5,6}
# setB = setA.copy()
# setB.add(10)
# print(setA)
# print(setB)

a = frozenset([1, 2, 3, 4])
print(a)
# a.add(5)
# a.remove(1)

