import re
filename = "input.txt"

with open(filename, "r") as f:
	line = f.readline().strip()
	total = 0
	while line:
		first = re.search("^[^\\d]*(\\d)", line).group(1)
		last = re.search("(\\d)[^\\d]*$", line).group(1)
		total += int(first+last)
		line = f.readline().strip()
	print(total)