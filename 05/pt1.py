import re
filename = "input.txt"
# filename = "example.txt"

def translate_with_maps(map_set, inputs):
	out = []
	for i in inputs:
		for m in map_set:
			src = m[1]
			dst = m[0]
			rng = m[2]
			if i in range(src, src+rng):
				# print("{} matches range {}-{} with output range {}-{}".format(i, src, src+rng, dst,dst+rng))
				# print("{} -> {}".format(i, (i + (dst-src))))
				i = i + (dst-src)
				break
		out.append(i)
	return out


with open(filename, "r") as f:
	line = f.readline().strip()
	current_set = [int(x) for x in re.search("seeds:\\s+([\\d ]+)", line)[1].split(" ")]
	line = f.readline().strip()
	stage = 0
	current_maps = []
	# print(current_set)
	while line or stage<7:
		if(line==""):
			pass
		elif(re.match(".* map:",line)):
			current_set = translate_with_maps(current_maps, current_set)
			# print("END STAGE " + str(stage))
			# print(current_set)
			stage+=1
			current_maps = []
		else:
			new_map = [int(x) for x in line.split(" ")]
			current_maps.append(new_map)
		line = f.readline().strip()
	current_set = translate_with_maps(current_maps, current_set)
	print(min(current_set))