class User :
    def log(self) :
        print("Users")

class Teacher(User) :
    def log(self) :
        print("I'am a teacher!")

class Customer(User) :
    def __init__(self, name, membership_type) :
        self.name = name
        self.membership_type = membership_type
        # print("customer created")

    def log(self) :
        print(self)

    @property
    def name(self) :
        print('getting name')
        return self._name # name is private

    @name.setter
    def name(self, name) :
        print('setting name')
        self._name = name

    @name.deleter
    def name(self) :
        del self._name

    def update_membership(self, new_membership) :
        print('Calculating costs')
        self.membership_type = new_membership

    def __str__(self) :
        # print("Converting to string")
        return self.name + " " + self.membership_type

    def print_all_customersc(customers) :
        for customer in customers :
            print(customer)

    def __eq__(self, other) :
        if self.name == other.name and self.membership_type==other.membership_type :
            return True
        return False  

    __hash__ = None

    __repr__ = __str__

    # def read_customer() :
    #     print("Reading customer from DB")

# c1 = Customer('scpark', "Gold")
# print(c1.name, c1.membership_type)

# c2 = Customer('Brad', 'Bronze')
# print(c2.name, c2.membership_type)

# customers = [c1, c2]

customers = [Customer('scpark', "Gold"), 
            Customer('Brad', 'Bronze'), 
            Teacher(), User()]

# print(customers[1].membership_type)          
# customers[1].update_membership('Silver')
# customers[1].membership_type = 'Gold'
# print(customers[1].membership_type)      

# print(customers[1])
# customers[1].verified = False
# print(customers[1].verified)  

# customers[0].read_customer()
# Customer.read_customer()
print("--------------")
# Customer.print_all_customersc(customers)

# print(customers[0] == customers[1])
# customers[0].name = "Caleb"
# customers[1].name = "Caleb"
# print(customers[0] == customers[1])

# data = {customers[0]}
print(customers)

customers[0].name = "GilDong Hong"
print(customers[0].name)
# print(customers[0].name()) # error
# del customers[0].name
print(customers[0].name)

customers[0].log()
customers[1].log()
customers[2].log()

print("************")

for user in customers :
    user.log()