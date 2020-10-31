# mydict = {"name":"Max", "age":29, "city":"New York"}
# print(mydict)

# mydict2 = dict(name="Mary", age=28, city="Boston")

# print(mydict2)
# print(mydict["name"])
# mydict["email"] = "max@xyz.com"
# print(mydict)

# del mydict["name"]
# print(mydict)

# mydict.pop("age")
# print(mydict)

# mydict.popitem()
# print(mydict)

# if "name" in mydict:
#     print(mydict["name"])

# try :
#     print(mydict["lastname"])
# except KeyError:
#     print("Error")    

# for key in mydict:
#     print(key) 
# print("--------------")
# for value in mydict.values():
#     print(value)     

# print("**************")
# for key, value in mydict.items():
#     print(key, ":", value)      

# mydict_copy = mydict
# print(mydict_copy)
# mydict_copy["email"] = "gdhong@abc.com"
# print(mydict)

# mydict_copy = mydict.copy()
# mydict_copy["email"] = "gdhong@abc.com"
# print(mydict_copy)
# print(mydict)

# mydict_copy = dict(mydict)
# mydict_copy["email"] = "gdhong@abc.com"
# print(mydict_copy)
# print(mydict)

# mydict = {"name":"Max", "age":28, "email":"max@xyz.com"}
# mydict2 = dict(name="Mary", age=27, city="Boston")

# mydict.update(mydict2)
# print(mydict)

my_dict = {3:9, 6:36, 9:81}
print(my_dict)

value = my_dict[3]
print(value) 

my_tuple = (8, 7)
my_dict = {my_tuple:15}
print(my_dict)
value = my_dict[my_tuple]
print(value)

my_list = [8, 7]
my_dict = {my_list: 15}  # list can't be used as a key of dictionary because it's mutable


