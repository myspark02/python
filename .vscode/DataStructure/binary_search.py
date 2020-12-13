import time


def elapsed_time(func) :
    def wrapper(*args, **kwargs) :
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__ + " took " + str((end_time-start_time)*1000) + " mil seconds")
        return result
    return wrapper

@elapsed_time
def linear_search(numbers_list, number_to_find) :
    # for index in range(len(numbers_list)) :
    #     if numbers_list[index] == number_to_find :
    #         return index
    # return -1

    for index, element in enumerate(numbers_list) :
        if element == number_to_find :
            return index
    return -1

@elapsed_time
def binary_search(numbers_list, number_to_find) :
    start = 0
    end = len(numbers_list)-1
    while start <= end :
        # mid = int((start+end)/2)
        mid = (start+end)//2
        if numbers_list[mid] == number_to_find :
            return mid
        elif numbers_list[mid] < number_to_find :
            start = mid + 1
        else :
            end = mid - 1
    
    return -1

# @elapsed_time            
def recursive_binary_search(numbers_list, number_to_find, start_index, end_index) :
    if start_index > end_index :
        return -1

    mid = (start_index+end_index)//2

    if numbers_list[mid] == number_to_find :
        return mid

    if numbers_list[mid] < number_to_find :
        return recursive_binary_search(numbers_list, number_to_find, mid+1, end_index)
    else :
        return recursive_binary_search(numbers_list, number_to_find, start_index, mid-1)

def find_all_occurrences(numbers, number_to_find) :
    index = binary_search(numbers, number_to_find)
    indices = [index]
    if index == -1 :
        return indices
    
    i = index - 1
    while i >= 0 :
        if numbers[i] == number_to_find :
            indices.append(i)
        else :
            break
        i -= 1
        
    
    i = index+1
    while i < len(numbers) :
        if numbers[i] == number_to_find :
            indices.append(i)
        else :
            break
        i += 1

    return sorted(indices)

if __name__ == '__main__' :
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 67
    # number_to_find = 456

    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 1000000
    index = linear_search(numbers_list, number_to_find)
    print(f'Number found at index {index} using linear search ')

    index = binary_search(numbers_list, number_to_find)
    print(f'Number found at index {index} using binary search ')

    index = recursive_binary_search(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f'Number found at index {index} using recursive binary search ')


    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    indices = find_all_occurrences(numbers, number_to_find)
    print(f'Indices of occurrences of {number_to_find} are {indices}')
