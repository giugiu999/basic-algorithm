from collections import deque, defaultdict

def bfs_tree(graph, start):
    """
    Perform BFS on the graph and construct the BFS tree.
    
    :param graph: dict, adjacency list representation of the graph
    :param start: starting node
    :return: tuple (predecessors, distances)
    """

    distances = {node: float('inf') for node in graph}  # d
    predecessors = {node: None for node in graph}       # pred
    distances[start] = 0
    queue = deque([start])                 

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):     # white
                distances[neighbor] = distances[current] + 1
                predecessors[neighbor] = current        # record pred
                queue.append(neighbor)
    
    return predecessors, distances

def print_bfs_tree(predecessors):
    """
    Print the BFS tree in a human-readable form.
    
    :param predecessors: dict, the BFS predecessors table
    """
    print("BFS Tree:")
    for node, parent in predecessors.items():
        if parent is None:
            print(f"Node {node} is the root.")
        else:
            print(f"Node {node} is a child of Node {parent}.")

# testing
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2, 6],
    5: [2],
    6: [4]
}

start_node = 1
predecessors, distances = bfs_tree(graph, start=start_node)

print_bfs_tree(predecessors)
