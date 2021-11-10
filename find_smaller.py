def findSmallest(arr):
    smallest = arr[0] # Для хранения наименьшего значения
    smallest_index = 0 # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
print (findSmallest([5, 3, 6, 2, 10]))

            
