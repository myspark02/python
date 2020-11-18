from address import Address

class Person :
    def __init__(self, first, last, dob, phone, address) :
        self.first_name = first
        self.last_name = last
        self.date_of_birth = dob
        self.phone = phone
        self.addresses = []
        
        if isinstance(address, Address):
            self.addresses.append(address)
        elif isinstance(address, list) :
            for element in address :
                if not isinstance(element, Address) :
                    raise Exception("Invalid Address...")
            self.addresses = address
        else :
            raise Exception("Invalid Address...")

    def add_address(self, address) :
        if not isinstance(address, Address) :
            raise Exception("Invalid Address...")
        self.addresses.append(address)
    