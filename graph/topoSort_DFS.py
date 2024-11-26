#[a,b] --> a , then b
from collections import defaultdict

def findOrderDFS(n, prerequisites):
    graph = defaultdict(list)
    for task, pre in prerequisites:
        graph[pre].append(task)
    
    visited = [0] * n  # 0: white, 1: grey, 2: black
    topo_order = []    
    has_cycle = False  

    def dfs(node):
        nonlocal has_cycle
        if visited[node] == 1:  # grey, and cycle
            has_cycle = True
            return
        if visited[node] == 2:  # black
            return

        visited[node] = 1
        for neighbor in graph[node]:
            dfs(neighbor)
        visited[node] = 2 # black
        topo_order.append(node)

    for i in range(n):
        if visited[i] == 0:  
            dfs(i)
        if has_cycle: 
            return []

    # flip
    return topo_order[::-1]

n = 6
prerequisites = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
]
print(findOrderDFS(n, prerequisites)) 

# cycle case
n = 3
prerequisites = [
    [1, 0],
    [0, 2],
    [2, 1],  # cycle
]
print(findOrderDFS(n, prerequisites))
