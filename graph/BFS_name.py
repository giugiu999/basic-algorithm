from collections import deque

def shortest_path_in_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r,l,u,d
    queue = deque([(*start, 0)])  # (x, y, distance)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, dist = queue.popleft()
        
        # loop termination
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    
    return -1  # no destination

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  
end = (4, 4)

print("Shortest path length:", shortest_path_in_maze(maze, start, end))
