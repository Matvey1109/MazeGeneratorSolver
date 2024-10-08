## Maze generators

### Binary Tree

For each grid cell in turn (from south to north and from west to east), a path is built to the neighboring cell to the east or north.
A diagonal structure is typical, stretching from the southwest to the northeast. The northern row and eastern column always turn out to be corridors without walls.

### Wilson's

We select a random cell and add it to the maze. Then we build a random path from any other cell. When the path runs into a cell that has already been added to the maze, the entire path is added to the maze. We create such random paths until all cells are in the maze. This algorithm is slow at first, but it speeds up with each added cell. There is no distinctive structure or features because it generates a completely random maze.

## Maze solvers

### BFS

Explores a grid-based maze by initializing a queue with the starting position and iteratively dequeuing paths. It checks the last position of the current path to see if it matches the endpoint; if so, it returns the path. For each position, it evaluates four possible movements (right, down, left, up) to find valid, non-wall cells not already in the current path. New paths are created by appending valid next positions to the current path, which are then enqueued for further exploration until the endpoint is reached.

### DFS

Explores a grid-based maze using a stack to manage paths. It begins by pushing the starting position onto the stack along with the corresponding path. The algorithm continues by popping the last position and its path from the stack, checking if it matches the endpoint; if it does, the path is returned. For each position, it evaluates four potential movements (right, down, left, up), ensuring the next cell is within bounds, not a wall, and not already in the current path. Valid next positions are then pushed onto the stack with their updated paths, allowing the search to proceed until the endpoint is reached.
