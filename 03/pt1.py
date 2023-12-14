import re
filename = "input.txt"
# filename = "example.txt"

grid = []
total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	grid = []
	while line:
		grid.append("."+line+".")
		line = f.readline().strip()

total=0
for i,line in enumerate(grid):
	prevline = "."*len(line)
	if(i!=0): prevline = grid[i-1]
	nextline = "."*len(line)
	if(i+1!=(len(grid))): nextline = grid[i+1]
	while m := re.search("(\\d+)", line):
		val = int(m[1])
		# print(m[1])
		# print(m.span(1))
		adj = line[m.start(1)-1] + line[m.end(1)] + prevline[m.start(1)-1:m.end(1)+1] + nextline[m.start(1)-1:m.end(1)+1]
		if(re.search("[^.1234567890]", adj)):
			# print("MATCH", val, adj)
			# print(re.search("[^.1234567890]", adj)[0])
			total+=val
		line = line[:m.start(1)] + "."*len(m[1])+line[m.end(1):]
print(total)