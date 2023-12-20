filename = "input.txt"
# filename = "example.txt"

def find_mirrors(grid):
	h = find_horizontal_mirrors(grid)
	rotated = ["".join([r[i] for r in grid[::-1]]) for i in range(len(grid[0]))]
	v = find_horizontal_mirrors(rotated)
	return (h*100)+v

def find_horizontal_mirrors(grid):
	total=0
	for ri in range(len(grid)-1):
		if(grid[ri] == grid[ri+1]):
			# possible mirror
			mirror_size = min(ri+1, len(grid)-(ri+1))
			is_mirror = True
			for j in range(1,mirror_size):
				if grid[ri-j] != grid[ri+j+1]:
					is_mirror=False
					break
			if(is_mirror):total+=ri+1
	return total

total=0
with open(filename, "r") as f:
	while True:
		grid = []
		line = f.readline().strip()
		if( not line) : break
		while line:
			grid.append(line)
			line = f.readline().strip()
		# print("\n".join(grid))
		m_count = find_mirrors(grid)
		# print(m_count)
		total+=m_count

print(total)