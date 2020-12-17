import random

def merge_two_sorted_list(arr1 : list, arr2 : list, org : list) -> None :

    i = j = idx = 0
    len1 = len(arr1)
    len2 = len(arr2)

    while i < len1 and j < len2 :
        if arr1[i] <= arr2[j] :
            org[idx] = arr1[i]
            i+=1
        else :
            org[idx] = arr2[j]
            j+=1
        idx+=1

    
    while i < len1 :
        org[idx] = arr1[i]
        i+=1
        idx+=1
    
    while j < len2 :
        org[idx] = arr2[j]
        j+=1
        idx+=1
    
def merge_sort(arr : list) -> None :
    if len(arr) <= 1 : 
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, arr)


if __name__ == '__main__' :
    arr = []

    for i in range(20) :
        arr.append(random.randint(1, 100))

    print(arr)
    merge_sort(arr)
    print(arr)