import re
from math import gcd
from functools import reduce

filename = "input.txt"
# filename = "example2.txt"

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

keys = [x for x in filter(lambda y: y[2]=="A", maps.keys())]
# print(keys)
steps_to_first_z = []
for k in keys:
	steps = 0
	while k[2] != "Z":
		for i in instructions:
			k = maps[k][i]
			steps += 1
			if(k[2] == "Z"):
				break
	steps_to_first_z.append(steps)
# print(steps_to_first_z)

# Find greatest common multiple of all numbers
# by multiplying them all together and dividing by GCDs
print(reduce(lambda x,y: int(x*y/gcd(x,y)), steps_to_first_z))