import re
filename = "input.txt"
# filename = "example.txt"

card_counts = [0, 1]
with open(filename, "r") as f:
	line = f.readline().strip()
	current_card = 1
	while line:
		if(current_card >= len(card_counts)): card_counts.append(1)
		current_card_multiples = card_counts[current_card]
		# print(line)
		match = re.search("Card\\s+\\d+:\\s+([\\d ]+)\\s+\\|\\s+([\\d ]+)\\s?", line)
		winners = set(re.split("\\s+", match[1]))
		have = set(re.split("\\s+", match[2]))
		# print(winners)
		# print(have)
		overlap = (winners & have)
		for x in range(1, len(overlap)+1):
			if(current_card+x >= len(card_counts)):
				card_counts.append(1) # original copy
			card_counts[current_card+x] += current_card_multiples
		current_card += 1
		line = f.readline().strip()
	print(sum(card_counts))