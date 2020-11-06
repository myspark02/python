import json
from typing import Dict


# class User :
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age

# user = User('Max', 27)    

# from json import JSONEncoder
# class UserEncoder(JSONEncoder) :
#     def default(self, obj) :
#         if isinstance(obj, User) :
#             return {'name':obj.name, 'age':obj.age, obj.__class__.__name__:True}
#         return JSONEncoder.default(self, obj)

# userJSON = UserEncoder().encode(user)
# userJSON = json.dumps(user, cls=UserEncoder)
# print(userJSON)

# def decode_user(dict) :
#     if User.__name__ in dict :
#         return User(name=dict['name'], age=dict['age'])    
#     return dict    

# user = json.loads(userJSON, object_hook=decode_user)
# print(user.name)
# print(type(user))
# user = json.loads(userJSON)
# print(type(user))


# def encode_user(obj) :
#     if isinstance(obj, User) :
#         return {'name':obj.name, 'age':obj.age, obj.__class__.__name__:True}
#     else:
#         raise TypeError('Object of non User type is not JSON serializable')

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

# person = {"name":"John", "age":30, "city":"New York", "hasChildren":False, "titles":["engineer", "programmer"]}
# personJSON = json.dumps(person, indent=4, sort_keys=True)
# personJSON = json.dumps(person, indent=4, separators=('; ', '= '))
# personJSON = json.dumps(person, indent=4)
# print(personJSON)

# with open("person.json", "r") as file:
#     person = json.load(file)
#     print(person)

# person = json.loads(personJSON)
# print(person)

print(p)
# with  open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)
    # json.dump(person, file)