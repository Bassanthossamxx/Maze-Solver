from pyamaze import maze, agent, COLOR


def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath


# Customize the maze
m = maze(25, 25)
m.CreateMaze(loopPercent=70)

# Solve the maze with DFS
path = DFS(m)

# Add customized agents with colors
a2 = agent(m, footprints=True, shape='square', color=COLOR.blue)

# Trace the paths with a delay for visualization
m.tracePath({a2: path}, delay=15)  # Removed color argument

# Run the visualization
m.run()
