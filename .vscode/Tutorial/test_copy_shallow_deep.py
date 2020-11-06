import copy

class Person :
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Company :
    def __init__(self, boss, employee) -> None:
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
# company_clone = copy.copy(company) #shallow copy
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56

print(company_clone.boss.age)
print(company.boss.age)
# p2.age = 28

# print(p2.age)
# print(p1.age)


# org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
# # cpy = copy.copy(org)
# cpy = copy.deepcopy(org)
# cpy[0][1] = -10
# print(cpy)
# print(org)


# org_list = [0,1, 2, 3, 4,]
# cpy_list = copy.copy(org_list)
# cpy_list = org_list.copy()
# cpy_list = org_list[:]
# cpy_list[0] = -10
# print(cpy_list)
# print(org_list)

# org_list = [0, 1, 2, 3, 4]
# cpy_list = org_list

# cpy_list[0] = -10

# print(org_list)
# print(cpy_list)

# org = 5
# cpy = org

# cpy = 6

# print(cpy)
# print(org)