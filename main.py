from pyamaze import maze, agent, COLOR


def solve_maze(m):
	# Start from the bottom right corner
	start = (m.rows, m.cols)

	# Initialize lists to keep track of explored cells and the path
	explored = [start]
	path_track = {}

	# List to explore cells
	to_explore = [start]

	# Keep exploring until we reach the goal (top-left corner)
	while to_explore:
		# Get the current cell
		current_cell = to_explore.pop()

		# Stop if we've reached the goal
		if current_cell == (1, 1):
			break

		# Check all possible directions
		for direction in ['E', 'W', 'S', 'N']:
			# Check if we can move in this direction
			if m.maze_map[current_cell][direction] == True:
				# Calculate the next cell based on direction
				if direction == 'E':
					next_cell = (current_cell[0], current_cell[1] + 1)
				elif direction == 'W':
					next_cell = (current_cell[0], current_cell[1] - 1)
				elif direction == 'S':
					next_cell = (current_cell[0] + 1, current_cell[1])
				else:  # North
					next_cell = (current_cell[0] - 1, current_cell[1])

				# Skip if we've already explored this cell
				if next_cell in explored:
					continue

				# Mark as explored and add to exploration list
				explored.append(next_cell)
				to_explore.append(next_cell)

				# Keep track of the path
				path_track[next_cell] = current_cell

	# Reconstruct the path from start to goal
	final_path = {}
	current = (1, 1)
	while current != start:
		# Get the previous cell in the path
		previous = path_track[current]
		# Create path from previous to current
		final_path[previous] = current
		# Move to previous cell
		current = previous

	return final_path


# Create the maze
m = maze(20, 20)  # 20x20 maze
m.CreateMaze(loopPercent=50)  # Create maze with some loops

# Solve the maze
path = solve_maze(m)

# Create an agent to show the path
maze_solver = agent(m, footprints=True, shape='square', color=COLOR.blue)

# Trace the path
m.tracePath({maze_solver: path}, delay=20)

# Run the maze visualization
m.run()