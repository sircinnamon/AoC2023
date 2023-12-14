import re
filename = "input.txt"

with open(filename, "r") as f:
	line = f.readline().strip()
	total = 0
	while line:
		line = line.replace("one", "o1e")
		line = line.replace("two", "t2o")
		line = line.replace("three", "t3e")
		line = line.replace("four", "f4r")
		line = line.replace("five", "f5e")
		line = line.replace("six", "s6x")
		line = line.replace("seven", "s7n")
		line = line.replace("eight", "e8t")
		line = line.replace("nine", "n9e")
		first = re.search("^[^\\d]*(\\d)", line).group(1)
		last = re.search("(\\d)[^\\d]*$", line).group(1)
		total += int(first+last)
		line = f.readline().strip()
	print(total)