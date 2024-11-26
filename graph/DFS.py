def dfs(graph):
    """
    Perform DFS on a graph and record discovery/finish times and predecessors.
    
    :param graph: dict, adjacency list representation of the graph
    :return: tuple (discovery_times, finish_times, predecessors)
    """
    discovery_times = {}
    finish_times = {}
    predecessors = {}
    colors = {}
    time = [0]  # global time variable

    for node in graph:
        colors[node] = "WHITE"
        predecessors[node] = None

    def dfs_visit(node):
        nonlocal time
        colors[node] = "GRAY"
        time[0] += 1
        discovery_times[node] = time[0]

        for neighbor in graph[node]:
            if colors[neighbor] == "WHITE":
                predecessors[neighbor] = node
                dfs_visit(neighbor)

        colors[node] = "BLACK"
        time[0] += 1
        finish_times[node] = time[0]

    for node in graph:
        if colors[node] == "WHITE":
            dfs_visit(node)

    return discovery_times, finish_times, predecessors


# testing
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [6],
    5: [],
    6: []
}

discovery_times, finish_times, predecessors = dfs(graph)

print("Discovery Times:", discovery_times)
print("Finish Times:", finish_times)
print("Predecessors:", predecessors)
