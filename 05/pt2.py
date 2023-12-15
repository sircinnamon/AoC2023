import re
filename = "input.txt"
# filename = "example.txt"

INT_MAX = 9999999999

def translate_with_maps(map_set, i):
	# print(map_set)
	for m in map_set:
		# print(m)
		if i >= m[0] and i < m[1]:
			return i+m[2]

def merge_maps(map_a, map_b):
	# print(map_a, "///",map_b)
	new_maps = []
	for pre_m in map_a:
		for post_m in map_b:
			input_start = post_m[0]
			input_end = post_m[1]
			post_input_range = range(input_start, input_end)
			# print("input start {}".format(input_start, input_end))
			# print("input end {}".format(input_end))
			output_start = pre_m[0]+pre_m[2]
			output_end = pre_m[1]+pre_m[2]
			pre_output_range = range(output_start, output_end)
			# print("output start {}".format(output_start))
			# print("output end {}".format(output_end))

			if(output_start in post_input_range and output_end-1 in post_input_range):
				# Case A: all inputs will hit this map
				new_maps.append([pre_m[0], pre_m[1], pre_m[2]+post_m[2]])
				# print("CASE A", new_maps[-1])
			elif(output_start in post_input_range):
				#Case B: some inputs will hit this map
				breakpnt = input_end - pre_m[2]
				new_maps.append([pre_m[0], breakpnt, pre_m[2]+post_m[2]])
				# print("CASE B", new_maps[-1])
			elif(output_end-1 in post_input_range):
				#Case C: some inputs will hit this map
				breakpnt = input_start - pre_m[2]
				new_maps.append([breakpnt, pre_m[1], pre_m[2]+post_m[2]])
				# print("CASE C", new_maps[-1])
			elif input_start in pre_output_range and input_end-1 in pre_output_range:
				#Case D: all things hitting that map come from this map
				breakpnt_a = input_start - pre_m[2]
				breakpnt_b = input_end - pre_m[2]
				new_maps.append([breakpnt_a, breakpnt_b, pre_m[2]+post_m[2]])
				# print("CASE D", new_maps[-1])
			else:
				# Nothing from this map hits that map
				pass
	return new_maps

def fill_map(m):
	# Fill gaps in a map with shift 0
	if(m[0][0] != 0):
		m = [[0,m[0][0],0]]+m
	if(m[-1][1] != INT_MAX):
		m = m+[[m[-1][1],INT_MAX,0]]
	new_m = []
	for i,segment in enumerate(m):
		if(i==0):
			new_m.append(segment)
			continue
		prev_segment = m[i-1]
		if(segment[0] != prev_segment[1]):
			new_m.append([prev_segment[1], segment[0], 0])
		new_m.append(segment)
	return(new_m)

seeds = []
with open(filename, "r") as f:
	line = f.readline().strip()
	seeds = [int(x) for x in re.search("seeds:\\s+([\\d ]+)", line)[1].split(" ")]
	line = f.readline().strip()
	stage = 0
	current_maps = []
	all_maps = []
	# print(current_set)
	while line or stage<7:
		if(line==""):
			pass
		elif(re.match(".* map:",line)):
			# current_set = translate_with_maps(current_maps, current_set)
			current_maps.sort(key=lambda x: x[0])
			all_maps.append(current_maps)
			# print("END STAGE " + str(stage))
			# print(current_set)
			stage+=1
			current_maps = []
		else:
			new_map = [int(x) for x in line.split(" ")]
			# REFORMAT MAP as input_start, input_end, shift
			new_map = [new_map[1], new_map[1]+new_map[2], new_map[0]-new_map[1]]
			current_maps.append(new_map)
		line = f.readline().strip()


# print(all_maps)
base_map = [[0, INT_MAX, 0]]
master_map = merge_maps(base_map, fill_map(all_maps[1]))
for mp in all_maps[2:]:
	master_map = merge_maps(master_map, fill_map(mp))
	# print(master_map)

# print(master_map)
# quit()
min_loc = INT_MAX
for i,s in enumerate(seeds[::2]):
	seed_max = s+seeds[(i*2)+1]-1
	min_loc = min(min_loc, translate_with_maps(master_map, s))
	min_loc = min(min_loc, translate_with_maps(master_map, seed_max))
	for mm in master_map:
		if(mm[0] in range(s, seed_max)):
			min_loc = min(min_loc, translate_with_maps(master_map, mm[0]))
print(min_loc)