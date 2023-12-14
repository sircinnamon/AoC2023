import re
filename = "input.txt"
# filename = "example.txt"

with open(filename, "r") as f:
	line = f.readline().strip()
	games = []
	while line:
		maxes = [0,0,0] # RGB
		for rnd in line.split(":")[1].split(";"):
			# print("\t"+rnd)
			if "red" in rnd:
				r = int(re.search("(\\d+) red", rnd).group(1))
				if r > maxes[0]: maxes[0]=r
			if "green" in rnd:
				g = int(re.search("(\\d+) green", rnd).group(1))
				if g > maxes[1]: maxes[1]=g
			if "blue" in rnd:
				b = int(re.search("(\\d+) blue", rnd).group(1))
				if b > maxes[2]: maxes[2]=b
			# print(maxes)
		games.append(maxes)

		line = f.readline().strip()
	total=0
	for g in games:
		total += g[0]*g[1]*g[2]
	# print(games)
	print(total)