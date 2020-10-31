# String : ordered, immutable, text representation

from timeit import default_timer as timer


# mystring="Hello World"
# mystring = 'Hello World!'
# print(mystring)

# mystring = """Hello
# World!!!"""
# print(mystring)

# mystring = "Hello \
# World!!!"
# print(mystring)

# mystring = "Hello World!"
# c = mystring[0]
# print(c)
# c = mystring[-1]
# print(c)

# substring = mystring[::-1]
# print(substring)

# if "World" in mystring:
#     print("Yes")

mystring = '            Hello World     '
mystring = mystring.strip()
# print(mystring)
# print(mystring.upper())
# print(mystring.startswith("He"))
# print(mystring.endswith("He"))
# print(mystring.find("o"))
# print(mystring.index("Wo"))
# print(mystring.count("o"))

# print(mystring.replace("World", "Universe"))

# mylist = mystring.split()
# print(mylist)
# newstring = ''.join(mylist)
# print(newstring)
# newstring = ' '.join(mylist)
# print(newstring)

# mylist = ["a"] * 1000000


# bad code
# start = timer()
# mystring = ""
# for i in mylist:
#     mystring += i

# print(mystring)
# end = timer()
# print(end-start)

# good code
# start = timer()
# mystring = ''.join(mylist)
# print(mystring)
# end = timer()
# print(end-start)

# %, format(), f-Strings
# var = "Tom"
# mystring = "the variable is %s" % var
# print(mystring)

# var = 3
# mystring = "the variable is %d" %var
# print(mystring)

# var = 3.12345678
# mystring = "the variable is %f" %var
# print(mystring)

# var = 3.12345678
# mystring = "the variable is %.2f" %var
# print(mystring)

# var = 3.12345678
# mystring = "the variable is {}".format(var)
# print(mystring)

# var = 3.12345678
# mystring = "the variable is {:.2f}".format(var)
# print(mystring)

# var = 3.12345678
# var2 = 6
# mystring = "the variable is {:.2f} and {}".format(var, var2)
# print(mystring)

var = 3.12345678
var2 = 6
mystring = f"the variable is {var*2} and {var2}"
print(mystring)