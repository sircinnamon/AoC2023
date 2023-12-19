filename = "input.txt"
# filename = "example.txt"

def dist(pta, ptb):
	# (x,y)
	return abs(pta[0]-ptb[0]) + abs(pta[1]-ptb[1])

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
		blank_rows.append(i+len(blank_rows))

for i in range(len(grid[0])):
	c = "".join(list([x[i] for x in grid]))
	if len(c.replace(".","")) == 0:
		blank_cols.append(i+len(blank_cols))

# print(blank_cols, blank_rows)

for c in blank_cols:
	for i,r in enumerate(grid):
		grid[i] = r[:c]+"."+r[c:]

for r in blank_rows:
	grid.insert(r, "."*len(grid[0]))

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