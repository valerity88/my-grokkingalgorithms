# Граф
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}


# Таблица стоимости
infinity = float("inf")
costs= {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Таблица соседей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = "None"
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Перебать узлы
    for node in costs:
        cost = costs[node]
        # Если этот узел с наименьшей стоимостью из уже виденных
        # и он еще не был обработан...
        if cost < lowest_cost and node not in processed:
            # ...он назначается новым узлом с наменьшей стоимостью
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# Ели обработаны все узлы, цикл while завершен
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # Перебрать всех соседей текущего узла
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Если к соседу можно быстрее добраться через текущий узел...
        if costs[n] > new_cost:
            # ...обновить стоимость для этого узла
            costs[n] = new_cost
            # Этот узел становится новым родителем для соседа
            parents[n] = node
    # Узел помечается как обработанный
    processed.append(node)
    # Найти следующий узел для обработки и повторить цикл
    node = find_lowest_cost_node(costs)
print(graph)    
print("Стоимость от начала до каждого узла")
print(costs) 
