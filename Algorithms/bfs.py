from collections import deque

def bfs(adj_list, num_nodes, source):
    visited = [False] * num_nodes
    distances = [0] * num_nodes
    parents = [-1] * num_nodes
    queue = deque()

    queue.append(source)
    visited[source] = True
    distances[source] = 0

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distances[neighbor] = distances[node] + 1
                parents[neighbor] = node

    return distances, parents

def print_path(parents, target):
    if not visited[target]:
        print("No path!")
    else:
        path = []
        while target != -1:
            path.append(target)
            target = parents[target]
        path.reverse()
        print("Path:", end=" ")
        print(*path)

num_nodes = 0  # number of nodes
source = 0  # source

adj_list = [[]]  # adjacency list representation

distances, parents = bfs(adj_list, num_nodes, source)

target_node = 0  # node for which you want to print the path
print_path(parents, target_node)
