class MyRange :
    def __init__(self, start, end) :
        self.value = start
        self.end = end

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end) :
    for i in range(start, end) :
        yield i

nums = my_range(1, 10)
for num in nums :
    print(num)

# print(next(nums))

# nums = MyRange(1, 10)

# for num in nums:
#     print(num)


# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


# nums = [1, 2, 3]

# i_nums = nums.__iter__()
# i_nums = iter(nums)  # The same as the above code

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# while True :
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration :
#         break        

# print(i_nums)
# print(dir(i_nums))

# for num in nums :
#     print(num)

# print(dir(nums))
# print(next(nums))