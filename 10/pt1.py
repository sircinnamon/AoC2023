from collections import deque
filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

visited = {}
check_adj = deque()
for y,row in enumerate(grid):
	if "S" in row:
		x = row.index("S")
		check_adj.append((x, y))
		visited[(x, y)] = 0

while len(check_adj) > 0:
	current = check_adj.popleft()
	x = current[0]
	y = current[1]
	pipe = grid[y][x]
	dist = visited[current]+1
	def visit(xprime,yprime):
		if((xprime,yprime) not in visited):
			visited[(xprime,yprime)] = dist
			check_adj.append((xprime,yprime))
			# print("{} appending {}".format((x,y), (xprime,yprime)))
	# north
	if pipe in "|LJ":
		visit(x,y-1)
	# east
	if pipe in "-LF":
		visit(x+1,y)
	# south
	if pipe in "|7F":
		visit(x,y+1)
	# west
	if pipe in "-J7":
		visit(x-1,y)
	# start
	if pipe == "S":
		if grid[y-1][x] in "|7F":
			visit(x,y-1)
		if grid[y+1][x] in "|LJ":
			visit(x,y+1)
		if grid[y][x-1] in "-LF":
			visit(x-1,y)
		if grid[y][x+1] in "-J7":
			visit(x+1,y)

# print(visited)
print(max(visited.values()))