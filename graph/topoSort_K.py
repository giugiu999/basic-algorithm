# prerequisites courses question
# [a,b] -> first b, then a
# return a order which can include all courses
# empty if cycle exists

from collections import defaultdict, deque
def findOrder(numCourses, prerequisites):
    in_degree = [0] * numCourses
    graph = defaultdict(list)
    
    for course, pre in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    topo_order = []
    
    # topo sorting
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) == numCourses:
        return topo_order
    else:
        return []  # cycle

# testing
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(findOrder(numCourses, prerequisites)) 
