filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

# rotate clockwise 90 degrees
grid = ["".join([c[i] for c in grid]) for i in range(len(grid))]

def shift_left(row):
	if("#" in row):
		out = ""
		for sub in row.split("#"):
			out+=shift_left(sub)+"#"
		return out[:-1]
	if(len(row)==0):return ""
	return "O"*row.count("O") + "."*row.count(".")

grid = [shift_left(x) for x in grid]

# print("\n".join(grid))
load = 0
for row in grid:
	for i,spot in enumerate(row):
		if(spot=="O"):
			load+=(len(row)-i)
print(load)