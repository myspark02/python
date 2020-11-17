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

"""
HASH TABLE FUNCTIONS
"""

def get_keys(ht) :
    return ht.keys()

def has_key(ht, key) :
    return key in ht

def max_value(ht) :
    """
    assume all values are int
    """    

    mx = float("-inf")
    # for k, v in ht.items() :
    #     if v > mx :
    #         mx = v

    for v in ht.values() :
        if v > mx:
            mx = v
    
    return mx

def min_value(ht) :
    """
    assume all values are int
    """
    mn = float("inf")

    for v in ht.values() :
        if v < mn :
            mn = v
    return mn
