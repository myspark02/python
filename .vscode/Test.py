import sys
import timeit
import token
import tokenize 
import collections

person = {"name":"gildong", "age":18, "gender":"male"}
str = [f"{k}={v!r}" for k, v in person.items()]
print(str)
for k, v in person.items() :
    print(k, ":", v)


# def string_tokenizer(str) :
#     arr = []
#     for word in str :
#         arr.append(word)
#     return arr

# str = "Title: Golden Hour 2 Author: Lee Gookjong Do you know about medical reality in Korea? And do you know how the lives of medical doctors are? This book shows those concretely One day, I saw a TV show “ The joy of conversation”.  Dr. Lee Gookjong talked about 'doctor helicopter', and Severe Trauma Surgery doctors, etc. in the show.  After watching it, I became to want to know more about Korea’s medical reality. And that led me to read Dr. Lee Gookjong’s book Golden hour. The book starts by showing the situation of Korea's Severe Trauma Center. Many patients from general hospitals who needed to be treated in university hospitals' severe trauma centers were forced to return to the general hospitals.  Many patients treated in severe trauma centers who should be transferred to the general hospital's emergency center often couldn't have a chance to be treated there. This is due to the lack of hospital beds. During that process, many severe patients died. In Korea's medical situation, sometimes severe trauma patients use the emergency room’s hospital beds. If the number of severe trauma patients who use the emergency room’s hospital bed increases, patients who really need to use the emergency room may not be able to use it. I think this medical situation needs to be improved. In order to improve this situation, we should increase the number of Severe Trauma center’s hospital beds and distinguish between the Severe Trauma center and the emergency room clearly. The next subject of the book is the lives of severe trauma surgeons. A great number of severe trauma surgeons work for a long time and sometimes even fall down. To improve this medical situation in Korea, I think we need to establish a medical system which can attract many medical students to apply for the so-called department of avoiding studies such as severe trauma center. Through this book, I got to know many things about medical doctors, medical situation in Korea,  and we still have many things to improve the medical reality." 
# list = str.split()
# result = collections.Counter(list)
# cnt = 0
# for k, v in result.items() :
#     print(k)
#     cnt=cnt+1

# print("-----------")
# print(cnt)


def test_tuple() :
    #Tuples : ordered, immutable, allows duplicate elements
    mytuple = ("Max", 28, "Boston")
    print(mytuple)

    mytuple = "Max", 28, "Boston"
    print(mytuple)

    mytuple = ("Max")
    print(type(mytuple))

    mytuple = ("Max", )
    print(type(mytuple))

    mytuple = tuple(["Max", 28, "Boston"])
    print(mytuple)

    mytuple = ('gdhong', 18)
    name, age = mytuple
    print(name)
    print(age)

    mytuple = (0, 1, 2, 3, 4)
    i1, *i2, i3 = mytuple
    print(i1)
    print(i2)
    print(i3)

    mylist = [0, 1, 2, "hello", True]
    mytuple = (0, 1, 2, "hello", True)

    print(sys.getsizeof(mylist), "bytes")
    print(sys.getsizeof(mytuple), "bytes")

    print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
    print(timeit.timeit(stmt= "(0, 1, 2, 3, 4, 5)", number=1000000))

# test_tuple()    

def test_list() :     
    # Lists : ordered, mutable, allows duplicate elements

    mylist = [4, 3, 1, -1, -5, 10]

    new_list = sorted(mylist)

    print("new_list: " + str(new_list))
    print("mylist: " + str(mylist))

    mylist = [0] * 5
    print("mylist: " + str(mylist)) 
    mylist2 = [1, 2, 3, 4, 5]

    new_list = mylist + mylist2

    print("new_list: " + str(new_list))

    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = mylist[::2]
    print("a: " + str(a))

    a = mylist[::-1]
    print("a: " + str(a))

    b = [i*i for i in mylist]
    print("b: " + str(b))


