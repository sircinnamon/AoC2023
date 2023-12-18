from collections import deque
filename = "input.txt"
# filename = "example2.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

visited = {}
edges = []
check_adj = deque()
for y,row in enumerate(grid):
	if "S" in row:
		x = row.index("S")
		check_adj.append((x, y))
		visited[(x, y)] = []

while len(check_adj) > 0:
	current = check_adj.pop()
	x = current[0]
	y = current[1]
	pipe = grid[y][x]
	def visit(xprime,yprime):
		visited[(x,y)].append((xprime,yprime))
		if((xprime,yprime) not in visited):
			edges.append(((x,y),(xprime,yprime)))
			visited[(xprime,yprime)] = []
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
		elif grid[y+1][x] in "|LJ":
			visit(x,y+1)
		elif grid[y][x-1] in "-LF":
			visit(x-1,y)
		elif grid[y][x+1] in "-J7":
			visit(x+1,y)

# print(edges)
verts = [x[0] for x in edges]
verts.append(edges[-1][1]) # Final vert

# Remove "middle verts" from continuous straight edges
# This has a small impact on runtime, but improves worst case
clean_verts = []
for i,v in enumerate(verts):
	prev = verts[i-1]
	nxt = verts[(i+1)%len(verts)]

	# Is a part of a line
	if((v[0]*2)-prev[0] == nxt[0] and (v[1]*2)-prev[1] == nxt[1]):
		pass
	else:
		# Only keep corners
		clean_verts.append(v)
verts = clean_verts


def inside_test(pt):
	origin = (0,pt[1])
	intersects = 0
	for e in edges:
		if e[0][1] == e[1][1]:
			# Horizontal line, ignore it
			pass
		elif pt[1] > max(e[0][1], e[1][1]) or pt[1] <= min(e[0][1], e[1][1]):
			# print("pt {} non intersect with {}-{}".format(pt, e[0], e[1]))
			pass
		elif (pt[0] > e[0][0]):
			intersects+=1
	return intersects

def pnpoly(pt):
	# pt: (x,y)
	# edge: ((x1,y1),(x2,y2))
	nvert = len(verts)
	inside = False
	verty = [x[1] for x in verts]
	vertx = [x[0] for x in verts]
	testx = pt[0]
	testy = pt[1]
	for i in range(nvert):
		j = i-1
		if ( ((verty[i]>testy) != (verty[j]>testy)) and
			(testx < (vertx[j]-vertx[i]) * (testy-verty[i]) / (verty[j]-verty[i]) + vertx[i]) ):
			inside = not inside;
		pass
	return inside

contained = 0
min_x = min([x[0] for x in visited.keys()])+1
max_x = max([x[0] for x in visited.keys()])
min_y = min([x[1] for x in visited.keys()])+1
max_y = max([x[1] for x in visited.keys()])

for test_x in range(min_x, max_x):
	for test_y in range(min_y, max_y):
		if((test_x, test_y) in visited.keys()):
			continue
		# if(pnpoly((test_x+0.5,test_y+0.5))):
		# 	# print(test_x, test_y)
		# 	contained += 1
		if(inside_test((test_x, test_y))%2 == 1):
			# print(test_x, test_y)
			contained += 1
print(contained)