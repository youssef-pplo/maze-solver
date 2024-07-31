import heapq

# Constants
WALL = '#'
SPACE = ' '
START = 'S'
END = 'E'

def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()

def heuristic(a, b):
    # Use Manhattan distance as the heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, end), 0, start))
    came_from = {}
    g_score = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    g_score[start] = 0
    f_score = { (r, c): float('inf') for r in range(rows) for c in range(cols) }
    f_score[start] = heuristic(start, end)
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != WALL:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))
    
    return None

def solve_maze(maze):
    start, end = None, None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == START:
                start = (r, c)
            elif maze[r][c] == END:
                end = (r, c)
    
    if start is None or end is None:
        print("Start or End not found in the maze.")
        return
    
    path = a_star(maze, start, end)
    if path:
        for (r, c) in path:
            if maze[r][c] not in [START, END]:
                maze[r][c] = '*'
        print("Path found:")
    else:
        print("No path found.")
    
    print_maze(maze)

if __name__ == "__main__":
    # Example maze
    maze = [
        [START, SPACE, SPACE, SPACE, SPACE],
        [WALL, WALL, SPACE, WALL, END],
        [SPACE, SPACE, SPACE, WALL, SPACE],
        [SPACE, WALL, SPACE, SPACE, SPACE],
        [SPACE, SPACE, SPACE, WALL, SPACE]
    ]
    
    print("Original Maze:")
    print_maze(maze)
    solve_maze(maze)
