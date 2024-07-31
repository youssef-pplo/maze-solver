
# Maze Solver with A* Algorithm

This project implements a maze solver using the A* search algorithm in Python. The A* algorithm finds the shortest path in a maze from a starting point to an ending point.

## Features

- Solves mazes using the A* algorithm.
- Displays the maze with the solution path marked.

## Maze Format

The maze is represented as a 2D list where:
- `'#'` denotes walls.
- `' '` denotes empty spaces.
- `'S'` denotes the start point.
- `'E'` denotes the end point.
- `'*'` denotes the path found by the algorithm.

## Example Maze

```plaintext
S   E
## #
  ## 
#   #
```

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/youssef-pplo/maze-solver.git
   cd maze-solver
   ```

2. Run the script:

   ```sh
   python maze_solver.py
   ```

## How to Use

1. Modify the `maze` variable in `maze_solver.py` to set up your maze.
2. Ensure the maze contains one start (`'S'`) and one end (`'E'`) point.
3. Run the script to see the solution path in the maze.

