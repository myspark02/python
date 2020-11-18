from person import Person
from address import Address
# from enroll import Enroll
 

class Student(Person) :
    def __init__(self, first, last, dob, phone, address, international=False) : 
        super().__init__(first, last, dob, phone, address)
        self.international = international
        self.enrolled = []

    # def add_enrollment(self, enroll) :
    #     if not isinstance(enroll, Enroll) :
    #         raise Exception("Invalid Enroll...")

    def is_on_probation(self) :
        return False

    def is_part_time(self) :
        return len(self.enrolled) <= 3
 
address = Address('Korea', "KB", "Daegu", "Bukgu", "754023  ")
std = Student('P', 'SC', 1974, '010-123', address)        