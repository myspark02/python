
def testWhile() :
    i = 1
    while i <= 10 :
        print(i)
        i+=1
    print("Done with loop")    

testWhile()        

def tupleTest() :
    coordinates = [(4, 5), (6, 7), (80, 34)]
    coordinates[1] = 10
    print(coordinates[1])


def say_hi() :
    print("hi") ; print(" Hello")
    name = "scpark?"
    if name == "scpark" :
        print("scpark!")
    else :
        print("Who are you?")

    is_male = False
    is_tall = True
    if is_male and is_tall :
        print("you are a male or tall or both")
    elif is_male and not(is_tall) :
        print("You are a short male")    
    elif not(is_male) and is_tall:
        print("You are not a malle but are tall")    
    else :
        print("You neither male nor tall")    

        
def max_num(num1, num2, num3) :
    if num1 >= num2 and num1 >= num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else :
        return num3

# print(max_num(300, 40, 5))

def convertMonth2FullName() :
    monthConversions = {
        "Jan" : "January", 
        "Feb" : "February", 
        "Mar" : "March" , 
        "Apr" : "April", 
        "May" : "May" , 
        "Jun" : "June", 
        "Jul" : "July", 
        "Aug" : "August", 
        "Sep" : "September", 
        "Oct" : "October",
        "Nov" : "November",  
        "Dec" : "December"
    }

    print(monthConversions["Mar"])
    print(monthConversions.get("Luv", "Not a valid key"))


