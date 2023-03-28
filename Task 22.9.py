array = list(map(int, input("Введите числа через пробел: ").split()))
element = int(input("Введите любое число: "))

def increasing(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
increasing(array)

print(f"Отсортированный список: {array}")

def binary_search(array, element, left, right):
    if left > right:
        return f"Введенное число {element} отсутствует в списке"

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, element, 0, len(array)))
