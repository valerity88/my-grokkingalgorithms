# Поиск наименьшего значения в массиве
def findSmallest(arr):
    # Для хранения наименьшего значения
    smallest = arr[0]
    # Для хранения индекса наименьшего значения
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
# Сортирует массив
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # Находит наименьший элемент массива и добавляет его в новый массив
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

            
