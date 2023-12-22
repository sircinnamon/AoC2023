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
to_check = deque([((0,0), "E")])

dirmap = {
	"E": (1,0),
	"W": (-1,0),
	"N": (0,-1),
	"S": (0,1)
}

VERBOSE = False
while len(to_check) > 0:
	curr, d = to_check.popleft()
	if(curr[0] < 0 or curr[0] >= len(grid[0]) or curr[1] < 0 or curr[1] >= len(grid)):
		continue
	if(curr in visited and d in visited[curr]):
		# A laser on a node with a direction already seen will follow the same path
		continue


	node = grid[curr[1]][curr[0]]
	# print(curr, d, node)
	if node == "|" and d in "EW":
		to_check.append(((curr[0], curr[1]-1), "N"))
		to_check.append(((curr[0], curr[1]+1), "S"))
	elif node == "-" and d in "NS":
		to_check.append(((curr[0]+1, curr[1]), "E"))
		to_check.append(((curr[0]-1, curr[1]), "W"))
	elif node == "/":
		new_d = "N" # if E
		if(d=="W"):new_d="S"
		elif(d=="S"):new_d="W"
		elif(d=="N"):new_d="E"
		to_check.append(((curr[0]+dirmap[new_d][0], curr[1]+dirmap[new_d][1]), new_d))
	elif node == "\\":
		new_d = "N" # if W
		if(d=="E"):new_d="S"
		elif(d=="S"):new_d="E"
		elif(d=="N"):new_d="W"
		to_check.append(((curr[0]+dirmap[new_d][0], curr[1]+dirmap[new_d][1]), new_d))
	else:
		# Continue case
		to_check.append(((curr[0]+dirmap[d][0], curr[1]+dirmap[d][1]), d))

	if(curr in visited):
		visited[curr] += d
	else:
		visited[curr] = d
	if VERBOSE:
		for y in range(len(grid)):
			for x in range(len(grid[0])):
				if((x,y) in visited):
					print("#", end="")
				else:
					print(grid[y][x], end="")
			print("")
		print("")

# print(visited.keys())
print(len(visited.keys()))