# **Maze Solver Project**

#### **Overview**
- Generates and solves mazes programmatically.
- Uses `pyamaze` for maze creation and visualization.
- Demonstrates pathfinding and visualization techniques.

---

#### **Key Features**
1. **Maze Generation**  
   - Generates a maze of adjustable size.  
   - Includes loops for complexity (`loopPercent`).

2. **Maze Solving**  
   - Implements a custom pathfinding algorithm.  
   - Finds the shortest path from the start to the goal.  

3. **Visualization**  
   - Displays the solution using an animated agent.  
   - Path traced dynamically for better visualization.

---

#### **Code Workflow**
1. **Generate the Maze**  
   ```python
   m = maze(20, 20)  # Create a 20x20 maze
   m.CreateMaze(loopPercent=50)  # Add loops (50%)
   ```

2. **Solve the Maze**  
   - Start from the bottom-right cell `(rows, cols)`.  
   - Explore all possible paths to the top-left `(1, 1)`.  
   - Keep track of visited cells and reconstruct the path.

3. **Visualize the Solution**  
   ```python
   maze_solver = agent(m, footprints=True, shape='square', color=COLOR.blue)
   m.tracePath({maze_solver: path}, delay=20)
   m.run()
   ```

---

#### **Highlights of the Algorithm**
- **Pathfinding Logic**  
   - Explore neighbors in all directions (`E`, `W`, `N`, `S`).  
   - Mark visited cells to avoid loops.  
   - Backtrack to reconstruct the shortest path.  

- **Visualization**  
   - Agent follows the solution path dynamically.  
   - Customizable animations (`delay`, shape, color).

---

#### **Customizable Parameters**
- **Maze Dimensions**: `maze(rows, cols)`  
  Example: `m = maze(10, 10)` for a 10x10 maze.  

- **Complexity**: `loopPercent`  
  Example: `m.CreateMaze(loopPercent=30)` for fewer loops.  

- **Agent Style**: `shape`, `color`, `footprints`  
  Example: `shape='arrow'`, `color=COLOR.green`.

---

#### **Demo Visualization**
1. Maze is generated.
2. Agent starts at the bottom-right corner.
3. Solution path is dynamically traced to the top-left.
