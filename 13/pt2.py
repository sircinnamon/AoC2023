filename = "input.txt"
filename = "example.txt"

def find_mirrors(grid):
	h = find_horizontal_mirrors(grid)
	rotated = ["".join([r[i] for r in grid[::-1]]) for i in range(len(grid[0]))]
	v = find_horizontal_mirrors(rotated)
	return (h*100)+v

def find_horizontal_mirrors(grid):
	width = len(grid[0])
	grid = "".join(grid)
	for i in range(width,len(grid),width):
		lhs = grid[:i]
		rhs = grid[i:2*i]
		if(2*i >= len(grid)):
			lhs = lhs[-len(rhs):]
		rhs = "".join([rhs[j:j+width] for j in range(0, len(rhs), width)][::-1])
		# pt 1 solution
		# if(rhs == lhs):
		# 	return i//width
		if(len(list(filter(lambda x: x[0] != x[1], zip(lhs,rhs)))) == 1):
			return i//width
	return 0

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