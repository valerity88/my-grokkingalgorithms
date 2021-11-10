def binary_search(list_, item):
    # В переменных low и hight
    # хранятся границы той части списка,
    # в которой выполняется поиск 
    low = 0
    hight = len(list_) - 1
    # Пока эта часть не сократится до одного элемента...
    # проверяем средний элемент
    while low <= hight:
        mid = int((low + hight) / 2)
        guess = list_[mid]
        # Если значение найдено
        if guess == item:
            return mid
        # Если много
        if guess > item:
            hight = mid - 1
        # Если мало
        else:
            low = mid + 1
    # Если значение не существует
    return None
# А теперь протестируем функцию
my_list = [1, 3, 5, 7, 9]
# Вернется индекс искомого элемента
print (binary_search(my_list, 3))
# Вернется None, так как элемент отсутствует в списке
print (binary_search(my_list, -1))
