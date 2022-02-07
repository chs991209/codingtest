graph = {
    "A": ["B"],
    "B": ["A", "C", "H"],
    "C": ["B", "D"],
    "D": ["C", "E", "G"],
    "E": ["D", "F"],
    "F": ["E"],
    "G": ["D"],
    "H": ["B", "I", "J", "M"],
    "I": ["H"],
    "J": ["H", "K"],
    "K": ["J", "L"],
    "L": ["K"],
    "M": ["H"],
}

graph1 = {
    "A": ["B"],
    "B": ["A", "H", "C"],
    "C": ["B", "D"],
    "D": ["C", "E", "G"],
    "E": ["D", "F"],
    "F": ["E"],
    "G": ["D"],
    "H": ["B", "I", "J", "M"],
    "I": ["H"],
    "J": ["H", "K"],
    "K": ["J", "L"],
    "L": ["K"],
    "M": ["H"],
}


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


print(dfs(graph, "A"))
print(dfs(graph1, "A"))


# def bfs_1(graph, start_node):
#     visit = {}
#     queue = list()
#
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit[node] = True
#         queue.extend(graph[node])
#
#     return visit
#
# print(bfs_1(graph, "A"))
#
#


def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


print(bfs(graph, "A"))
#
