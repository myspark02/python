def shell_sort(arr:list) -> None:
    gap = len(arr) // 2
    while gap >= 1 : 
        for i in range(gap, len(arr)) :
            j = i - gap
            tmp = arr[i]
            while j >= 0 and arr[j] > tmp :
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = tmp
        gap = gap//2


if __name__ == '__main__' :
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)