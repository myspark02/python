"""
LIST FUNCTIONS
"""
def get_max(list) :
    mx = float("-inf")

    for num in list:
        if num > mx :
            mx = num

    return mx

def get_min(list) :
    mn = float("inf")

    for num in list :
        if num < mn :
            mn = num
    
    return mn

def get_average(list) :
    return sum(list) / len(list)

def get_median(list) :
    list = sorted(list)

    if len(list)%2 == 0 :
        return (list[(len(list)/2)-1] + list[(len(list)/2)])/2
    else :
        return list[(len(list)-1)/2]    