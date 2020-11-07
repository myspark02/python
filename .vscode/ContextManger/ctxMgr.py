# with opne('ctx.py') as f:
#     pass


from sqlite3 import connect

# with ctx() as x :
#     pass

# x = ctx().__enter__()
# try:
#     pass
# finally :
#     x.__exit__()

# class temptable :
#     def __init__(self, cur) :
#         self.cur = cur

#     def __enter__(self) :
#         print("__enter__")
#         self.cur.execute("create table points(x int, y int)")

#     def __exit__(self, *args) :
#         print("__exit__")
#         self.cur.execute("drop table points")

# with connect('test.db') as conn:
#     cur = conn.cursor() 
#     # cur.execute('create table points(x int, y int)')
#     with temptable(cur) :
#         cur.execute('insert into points(x, y) values(1, 1)')
#         cur.execute('insert into points(x, y) values(1, 2)')
#         cur.execute('insert into points(x, y) values(2, 1)')

#         for row in cur.execute('select x, y from points'):
#             # print(row[0], row[1])
#             print(row)

#     # cur.execute('drop table points')
#     conn.commit()

# class contextmanager :
#     def __init__(self, cur) :
#         self.cur = cur

#     def __enter__(self) :
#         print("__enter__")
#         self.gen = temptable(self.cur)
#         next(self.gen)

#     def __exit__(self, *args) :
#         print("__exit__")
#         next(self.gen)

from contextlib import contextmanager

@contextmanager
def temptable(cur) :
    print("create table")
    # yield cur.execute("create table points(x int, y int)")
    cur.execute("create table points(x int, y int)")
    # print("drop table")
    # yield cur.execute("drop table points")
    try :
        yield
    finally :
        print("drop table")
        cur.execute("drop table points")

with connect('test.db') as conn:
    cur = conn.cursor() 
    # gen = temptable(cur)
    # next(gen)
    # next(gen)
    # cur.execute('create table points(x int, y int)')
    # with contextmanager(cur) :
    with temptable(cur) :
        cur.execute('insert into points(x, y) values(1, 1)')
        cur.execute('insert into points(x, y) values(1, 2)')
        cur.execute('insert into points(x, y) values(2, 1)')

        for row in cur.execute('select x, y from points'):
            # print(row[0], row[1])
            print(row)

    # # cur.execute('drop table points')
    conn.commit()
