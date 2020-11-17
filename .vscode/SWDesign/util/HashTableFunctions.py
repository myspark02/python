"""
HASH TABLE FUNCTIONS
"""

def get_keys(ht) :
    return ht.keys()

def has_key(ht, key) :
    return key in ht

def get_max(ht) :
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

def get_min(ht) :
    """
    assume all values are int
    """
    mn = float("inf")

    for v in ht.values() :
        if v < mn :
            mn = v
    return mn
