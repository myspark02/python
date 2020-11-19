import sqlite3   

# conn = sqlite3.connect('customer.db')

# conn = sqlite3.connect(':memory:')

#create a cursor
# cursor = conn.cursor()

def show_all() :
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("select rowid, * from customers")

    for customer in cursor.fetchall() :
        print(customer)
    conn.commit()
    conn.close()


# add a new record to the table
def add_one(first, last, email) :
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("insert into customers values(?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

#add many records to table
def add_many(customers) :
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.executemany("insert into customers values(?,?,?)", customers)
    conn.commit()
    conn.close()

#delete a record from table, rowid should be given as string
def delete_one(rid) :
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()    
    cursor.execute("delete from customers where rowid= ?", rid)
    conn.commit()
    conn.close()

# Lookup with where clause
def email_lookup(email) :
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()    
    cursor.execute("select * from customers where email = ?", (email,))
    items = cursor.fetchall()

    for item in items :
        print(item)

    conn.commit()
    conn.close()


#Drop table
# cursor.execute("drop table customers")

# create a table
# sqlite3 has only 5 data types: NULL, INTEGER, REAL, TEXT, BLOB
# cursor.execute("""create table customers (
#         first_name text, 
#         last_name text, 
#         email text    
#     )""") # use doc string for multiple lines

# cursor.execute("insert into customers values('John', 'Lee', 'john@gmail.com')")
# cursor.execute("insert into customers values('Tim', 'Smith', 'tim@gmail.com')")
# cursor.execute("insert into customers values('Mary', 'Brown', 'mary@gmail.com')")

# many_customers = [
#             ('Wes', 'Brown', 'wes@gmail.com'), 
#             ('Steph', 'Kuewa', 'steph@gmail.com'), 
#             ('Dan', 'Pas', 'dan@gmail.com')
#         ]

# cursor.executemany('insert into customers values(?,?,?)', many_customers)        

# update records

# cursor.execute(""" update customers set first_name = 'SoRyong' 
#                     where last_name = 'Lee'
#         """)

# cursor.execute(""" update customers set first_name = 'GilDong' 
#                     where rowid = 2
#         """)

# cursor.execute("delete from customers where last_name = 'Pas'")

# cursor.execute('insert into customers values("SungChul", "Park", "scpark@gmail.com")')

# cursor.execute("select rowid, * from customers")

# cursor.execute("select rowid, * from customers order by rowid desc")

# cursor.execute("select * from customers where last_name='Smith'")

# cursor.execute("select rowid, * from customers where last_name like 'P%' and first_name ='SungChul'")
# cursor.execute("select rowid, * from customers where last_name like 'P%' or first_name ='GilDong'")
# cursor.execute("select rowid, * from customers limit 3")
# cursor.execute("select rowid, * from customers limit 1, 3")

# cursor.fetchone()
# cursor.fetchmany(3)
# print(cursor.fetchall())

# for customer in cursor.fetchall() :
#     print(customer)


# conn.commit()

#close our connection
# conn.close()