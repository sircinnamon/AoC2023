import re
filename = "input.txt"
# filename = "example.txt"

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		# print(line)
		match = re.search("Card\\s+\\d+:\\s+([\\d ]+)\\s+\\|\\s+([\\d ]+)\\s?", line)
		winners = set(re.split("\\s+", match[1]))
		have = set(re.split("\\s+", match[2]))
		# print(winners)
		# print(have)
		overlap = (winners & have)
		if(len(overlap)):
			# print(overlap)
			# print(pow(2, len(overlap)-1))
			total += pow(2, len(overlap)-1)
		line = f.readline().strip()
	print(total)