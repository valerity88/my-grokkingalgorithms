def quicksort(array):
    # Базовый случай: массивы с 0 и 1 элементом уже "отсортированы"
    if len(array) < 2:
        return array
    else:
        # Рекурсивный случай
        pivot = array[0]
        # Подмассив всех элементов меньших опорного
        less = [i for i in array[1:] if i <= pivot]
        # Подмассив всех элементов больших опорного
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
    
