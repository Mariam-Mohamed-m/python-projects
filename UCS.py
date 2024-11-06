def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost


def path_cost2(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]


def UCS(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path

        adjacent_nodes = graph.get(node, [])
        for (node2, cost) in adjacent_nodes:
            new_path = path.copy()
            new_path.append((node2, cost))
            queue.append(new_path)


# Define the graph
graph = {
    'S': [('A', 2), ('B', 3),('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1),('G',2)],
    'D': [('G', 5)],
    'G': []
}


solu = UCS(graph, 'S', 'G')


print("Result is:", solu)

print("Cost:", path_cost(solu))
