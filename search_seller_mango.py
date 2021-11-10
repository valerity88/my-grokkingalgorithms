from collections import deque
def person_is_seller(name):
    return name[-1] == 'm'
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom "] = []
graph["jonny"] = []
print(graph)
def search(name):
    # Создание новой очереди
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += graph["you"]
    # этот массив используется для отслеживания уже проверенных людей
    searched = [] 
    # Пока очередь не пуста
    while search_queue:
        # Из очереди извлекается первый человек
        person = search_queue.popleft()
        # Человек проверяется только в том случае, если он не проверялся ранее 
        if not person in searched:
            # Проверяем, является ли этот человек продавцом манго
            if person_is_seller(person):
                # Да, это продавец манго
                print(person + " - это продавец манго!")
                return True
            else:
                # Нет, не является.
                # Все друзья этого человека добавляются в очередь поиска
                search_queue += graph[person]
                # Человек помечается как уже проверенный
                searched.append(person)
    return False
search("you")

    
