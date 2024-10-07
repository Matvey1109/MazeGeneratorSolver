## Maze generators

### Binary Tree

For each grid cell in turn (from south to north and from west to east), a path is built to the neighboring cell to the east or north.
A diagonal structure is typical, stretching from the southwest to the northeast. The northern row and eastern column always turn out to be corridors without walls.

### Wilson's

We select a random cell and add it to the maze. Then we build a random path from any other cell. When the path runs into a cell that has already been added to the maze, the entire path is added to the maze. We create such random paths until all cells are in the maze. This algorithm is slow at first, but it speeds up with each added cell. There is no distinctive structure or features because it generates a completely random maze.
