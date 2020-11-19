import database

# database.add_one("Laura", "Smith", "laura@smith.com")
# database.add_one("Cherry", "Blue", "cherry@blue.com")

# database.delete_one(str(8))

# customers = [
#     ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
#     ('Joshua', 'Raintree', 'joshua@raintree.com'),
#     ('ChungHyang', 'Sung', 'ch@gmail.com')
# ]
# database.add_many(customers)

database.show_all()
print("------- email lookup ------")
database.email_lookup("ch@gmail.com")