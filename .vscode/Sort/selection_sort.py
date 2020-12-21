import random

def selection_sort(arr:list) -> None :
    for i in range(len(arr)-1) :
        min_index = i 
        for j in range(i+1, len(arr)) :
            if arr[j] < arr[min_index] :
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


elements = []

for i in range(10) :
    elements.append(random.randint(1, 100))

print(f'Before sorting {elements}')
selection_sort(elements)
print(f'After sorting {elements}')
