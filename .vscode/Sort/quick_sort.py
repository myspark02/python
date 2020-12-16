import random

def partition(elements : list, start : int, end : int) -> int :
    pivot = elements[start]

    i = start+1
    j = end
    
    while i < j :
        while i <= end and elements[i] < pivot :
            i+=1

        while elements[j] > pivot :
            j -= 1

        if i < j :
            elements[i], elements[j] = elements[j], elements[i] 
        else :
            break
    
    elements[j], elements[start] = elements[start], elements[j]

    return j

def quick_sort(elements : list, start : int, end : int) -> None :
    if start >= end :
       return 
    idx = partition(elements, start, end)
    quick_sort(elements, start, idx-1)
    quick_sort(elements, idx+1, end)


if __name__ == '__main__' :
    elements = []

    for i in range(10) :
        elements.append(random.randint(1, 100))
    
    print(elements)
    quick_sort(elements, 0, len(elements)-1)
    print(elements)