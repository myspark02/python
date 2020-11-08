import itertools
from itertools import repeat

# counter = itertools.count(start=5, step=-2.5)


# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]

# daily_data = list(zip(itertools.count(), data))
# daily_data = list(zip(range(10), data))
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)




# counter = itertools.cycle([1,2,3])
# counter = itertools.cycle(("On", "Off"))
# counter = itertools.repeat(2, times=3)

# squares = map(pow, range(10), itertools.repeat(2))
# squares = itertools.starmap(pow, [(0,2), (1,2), (2,2), (3,2)])
# print(list(squares))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']



# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, repeat=4)
# result = itertools.combinations_with_replacement(numbers, 4)
# cnt = 0
# for item in result :
#     print(item)
#     cnt+=1

# print(cnt)    

# combined = letters + numbers + names

# print(combined)

# combined = itertools.chain(letters, numbers, names)


# for item in combined:
#     print(item)

# result = itertools.islice(range(10), 5)
# result = itertools.islice(range(10), 1, 5)
# result = itertools.islice(range(10), 1, 5, 2)
# for item in result :
#     print(item)


# with open("test.log", "r") as f :
#     header = itertools.islice(f, 3) 
#     for line in header :
#         print(line, end='')


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

# result = itertools.compress(letters, selectors)
# for item in result :
#     print(item)

def lt_2(n) :
    if n < 2 :
        return True
    return False

# result = filter(lt_2, numbers)

# result = itertools.filterfalse(lt_2, numbers)

# for item in result :
#     print(item)

numbers = [0, 1, 2, 3, 2, 1, 0]

# result = itertools.dropwhile(lt_2, numbers)
# result = itertools.takewhile(lt_2, numbers)

# result = itertools.accumulate(numbers)

# for item in result :
#     print(item)

import operator
numbers = [1, 2, 3, 2, 1, 0]
result = itertools.accumulate(numbers, operator.mul)

# for item in result :
#     print(item)

def get_state(person) :
    return person['state']

people = [
    {'name': 'John Doe', 
     'city': 'Gotham', 
     'state': 'NY'}, 
    
    {'name': 'Jane Doe', 
     'city': 'Kings Landing', 
     'state': 'NY'}, 
    
    {'name': 'Jim Doe', 
     'city': 'Charlotte', 
     'state': 'NC'}, 
   
     {'name': 'Jane Taylor', 
     'city': 'Faketown', 
     'state': 'NC'},    

     {'name': 'Mark Kein', 
     'city': 'Asheville', 
     'state': 'NC'},           

     {'name': 'Corey Schafer', 
     'city': 'Seatle', 
     'state': 'NC'},                 
     
     {'name': 'Al Einstein', 
     'city': 'Denver', 
     'state': 'CO'},   
     
     {'name': 'John Henry', 
     'city': 'Hinton', 
     'state': 'WV'},        
     
     {'name': 'Nicole K', 
     'city': 'Asheville', 
     'state': 'NC'}
]

person_group = itertools.groupby(people, get_state)  # collections need to be sorted first to be grouped by! 

copy1, copy2 = itertools.tee(person_group) # when an iterator is copied then make sure not to use an original one!!!!
print(copy1, ", ",  copy2)
print(list(copy1))
print("********************")
print(list(copy2))
# for group in person_group :
#     print(group[0])
#     for person in group[1] :
#         print(person)
#     print()    

# for key, group in person_group :
#     print(key, len(list(group)))
    # for person in group :
    #     print(person)
    # print()

print("--------------------")
for key, group in copy1 :
    print(key, len(list(group)))

print("--------------------")
# for key, group in copy2 :
#     print(key, len(list(group)))