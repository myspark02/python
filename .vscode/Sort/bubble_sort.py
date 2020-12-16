
import random

def bubble_sort(arr : list) -> None :
    for i in range(len(arr)-1) :
        sorted = True
        for j in range(len(arr) - 1-i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted :
            print(f'Sorted in {i+1}th pass')
            break

def bubble_sort2(elements : list, key : str) -> None :
    for i in range(len(elements)-1) :
        sorted = True
        for j in range(len(elements) - 1-i) :
            if elements[j][key] > elements[j+1][key] :
                elements[j], elements[j+1] = elements[j+1], elements[j]
                sorted = False
        if sorted :
            print(f'Sorted in {i+1}th pass')
            break


if __name__ == '__main__' :
    arr = []
   
    for i in range(10) :
        arr.append(random.randint(1, 100))

    print(arr)

    bubble_sort(arr)

    print(arr)

    elements = [    
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print(elements)

    # bubble_sort(elements, key='transaction_amount')
    bubble_sort2(elements, key='name')

    print(elements)
