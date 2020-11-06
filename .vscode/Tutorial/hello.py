
from math import floor, sqrt

msg = "Hello World"
print(msg)
# print(len(msg))
# print(msg.index("W"))
# print(str(5) + " my favorite number")
# print(floor(5.9))
# print(sqrt(36))
# print("input")
#name = input("Enter your name: ")
#print("Hello " + name+ "!")



friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
friends.extend([4, 8, 15, 16, 23, 42])
friends.append("Creed")
friends.insert(1, "Kelly")
#friends.remove("Jim")
luckyNumbers = [4, 8, 15, 16, 23, 42]
print(luckyNumbers)
print("--------------")
luckyNumbers.sort()
print(luckyNumbers)
luckyNumbers.reverse()
print(luckyNumbers)
print("--------------")
print(friends)
print(friends.index("Oscar"))
print("# of Jim " + str(friends.count("Jim")))
friends.pop(0)
friends.clear()

print(friends2)


