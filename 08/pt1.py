import re
filename = "input.txt"
# filename = "example.txt"

instructions = []
maps = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	instructions = [1 if x == "R" else 0 for x in line]
	line = f.readline().strip() # blank
	line = f.readline().strip()
	while line:
		new_map = re.match("(...) = \\((...), (...)\\)", line)
		maps[new_map[1]] = [new_map[2], new_map[3]]
		line = f.readline().strip()
# print(maps)

key = "AAA"
steps = 0
while key != "ZZZ":
	for i in instructions:
		key = maps[key][i]
		steps += 1
		if(key=="ZZZ"): break
print(steps)