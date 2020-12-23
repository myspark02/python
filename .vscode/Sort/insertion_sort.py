import random

def insertion_sort(elements:list) -> None:
    length = len(elements)

    for i in range(1, length) :
        val = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > val :
            if (elements[j] > val) :
                elements[j+1] = elements[j]
            else :
                break
            j -= 1
        elements[j+1] = val


if __name__ == '__main__' :
    elements = []

for i in range(10) :
    elements.append(random.randint(1, 100))

print(elements)
insertion_sort(elements)
print(elements)