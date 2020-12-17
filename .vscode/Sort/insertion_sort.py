import random

def insertion_sort(elements:list) -> None:
    length = len(elements)

    for i in range(1, length) :
        val = elements[i]
        for j in range(i-1, -1, -1) :
            if (elements[j] > val) :
                elements[j+1] = elements[j]
            else :
                break
        elements[j] = val


if __name__ == '__main__' :
    elements = []

for i in range(10) :
    elements.append(random.randint(1, 100))

print(elements)
insertion_sort(elements)
print(elements)