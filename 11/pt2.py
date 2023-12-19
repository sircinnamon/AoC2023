filename = "input.txt"
# filename = "example.txt"

def dist(pta, ptb):
	# (x,y)
	dist = 0
	expansion = 1000000
	min_x = min(pta[0],ptb[0])
	max_x = max(pta[0],ptb[0])
	min_y = min(pta[1],ptb[1])
	max_y = max(pta[1],ptb[1])
	for x in range(min_x, max_x):
		# print(x)
		if x in blank_cols:
			dist+=expansion
		else: dist+=1
	for y in range(min_y, max_y):
		if y in blank_rows:
			dist+=expansion
		else: dist+=1
	return dist

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

blank_cols = []
blank_rows = []
for i,r in enumerate(grid):
	if len(r.replace(".","")) == 0:
		blank_rows.append(i)

for i in range(len(grid[0])):
	c = "".join(list([x[i] for x in grid]))
	if len(c.replace(".","")) == 0:
		blank_cols.append(i)

# print(blank_cols, blank_rows)

galaxies = []
for i,l in enumerate(grid):
	# print(l)
	ind = 0
	while True:
		gal = l.find("#",ind)
		if(gal != -1):
			galaxies.append((gal,i))
			ind = gal+1
		else: break

total = 0
for i,g in enumerate(galaxies):
	for g2 in galaxies[i+1:]:
		# print("{} to {} -> {}".format(g, g2, dist(g,g2)))
		total+=dist(g,g2)
print(total)