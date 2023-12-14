import re
filename = "input.txt"
# filename = "example.txt"
# filename = "temp.txt"
grid = []
total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	grid = []
	while line:
		grid.append("."+line+".")
		line = f.readline().strip()

total=0
gears = dict()
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
		if(line[m.start(1)-1] == "*"):
			gear = "{},{}".format(m.start(1)-1, i)
			if gear in gears:
				gears[gear].append(val)
			else:
				gears[gear] = [val]
		if(line[m.end(1)] == "*"):
			gear = "{},{}".format(m.end(1), i)
			if gear in gears:
				gears[gear].append(val)
			else:
				gears[gear] = [val]
		for j,c in enumerate(prevline[m.start(1)-1:m.end(1)+1]):
			if(c == "*"):
				gear = "{},{}".format(m.start(1)-1+j, i-1)
				if gear in gears:
					gears[gear].append(val)
				else:
					gears[gear] = [val]
		for j,c in enumerate(nextline[m.start(1)-1:m.end(1)+1]):
			if(c == "*"):
				gear = "{},{}".format(m.start(1)-1+j, i+1)
				if gear in gears:
					gears[gear].append(val)
				else:
					gears[gear] = [val]
		line = line[:m.start(1)] + "."*len(m[1])+line[m.end(1):]
# print(gears)
for g in gears:
	if len(gears[g]) == 2:
		# print("G "+g)
		# print("\t"+str(gears[g]))
		total+= gears[g][0]*gears[g][1]
print(total)