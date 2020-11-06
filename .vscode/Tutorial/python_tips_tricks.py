from getpass import getpass

#Tip 08
username = input("Username:")
# password = input("Password:")
password = getpass("Password:")

print('Logging in....')


#Tip 07
# class Person:
#     pass

# person = Person()

# person_info = {'first' : 'Corey', 'last':'Schafer'}

# for key, value in person_info.items() :
#     setattr (person, key, value)

# # print(person.first, person.last)

# for key in person_info.keys() :
#     print(getattr(person, key))
# person.first = 'Corey'
# person.last = 'Schafer'

# print(person.first)
# print(person.last)

# first_key = 'first'
# first_val = 'Corey'

# setattr(person, first_key, first_val)

# person.first_key = first_val

# first = getattr(person, first_key)
# print(person.first)
# print(first)

#Tip 06
#Normal 
# items = (1,2)
# print(items)

#Unpacking
# a, b = (1,2)
# print(a)
# print(b)

# a, _ = (1,2)
# print(a)

# a, b, *c = (1, 2, 3, 4, 5)
# a, b, *_ = (1, 2, 3, 4, 5)
# a, b, *c, d = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)
# print(d)

#Tip 05
# names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'Dc']

# # for index, name in enumerate(names) :
# #     hero = heroes[index]
# #     print(f'{name} is actually {hero}')

# # for name, hero, universe in zip(names, heroes, universes) : # stop at the shortest list..
# #     print(f'{name} is actually {hero} from {universe}')

# for value in zip(names, heroes, universes) : # stop at the shortest list..
#     print(value)



#Tip 04
# names = ['Corey', 'Chris', 'Dave', 'Travis']

# for index, name in enumerate(names) :
# for index, name in enumerate(names, start=1) :
#     print(index, name)


#Tip 03
    #context manager. No need to close a resource after using it.
# with open('test.txt', 'r') as f:
#     file_contents = f.read()

# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)

# Tip 02
# num1 = 10_000_000_000
# num2 =    100_000_000

# total = num1 + num2
# print(f'{total:,}')

# Tip 01
# condition = True

# x = 1 if condition else 0

# print(x)