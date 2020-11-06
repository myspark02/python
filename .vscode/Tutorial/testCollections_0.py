# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
d.insert(2, 10)     
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4, 5, 6])
print(d)
d.extendleft([1,2,3])
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)

# d = defaultdict(int)
# d = defaultdict(float)
# d = {'f': 7, 'y':10}
# d['a'] = 1
# d['d'] = 2
# d['c'] = 3
# d['b'] = 4
# print(d)
# print(d['c'])
# print(d['e'])

# ordered_dict = OrderedDict()
# ordered_dict = {}
# ordered_dict['b'] = 4
# ordered_dict['c'] = 3
# ordered_dict['a'] = 2
# ordered_dict['d'] = 1
# print(ordered_dict)



# Point = namedtuple('Point', 'x, y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)


# a = "aaaaaabbbbccc"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(1))
# print(list(my_counter.elements()))