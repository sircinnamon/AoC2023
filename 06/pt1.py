from functools import reduce
filename = "input.txt"
# filename = "example.txt"

def does_win(press_time, move_time, record):
	return ((press_time*move_time) > record)

times = []
dists = []
with open(filename, "r") as f:
	times = [int(x) for x in filter(lambda x: x!="", f.readline().strip().split(":")[1].split(" "))	]
	dists = [int(x) for x in filter(lambda x: x!="", f.readline().strip().split(":")[1].split(" "))]

# print(times)
# print(dists)
total_ways = []
for ri in range(len(times)):
	t = times[ri]
	rec = dists[ri]
	min_victory = t
	max_victory = 0
	center = round(t/2)
	for i in range(round(t/2)+1):
		min_test = center - i
		max_test = center + i
		if(min_test >= 0 and does_win(min_test, t-min_test, rec)):
			min_victory = min_test
		if(max_test < t and does_win(max_test, t-max_test, rec)):
			max_victory = max_test
		if(max_victory!=max_test and min_victory!=min_test):
			break
	# print("Win race: hold for {} to {} ms".format(min_victory, max_victory))
	total_ways.append((max_victory-min_victory)+1)
# print(total_ways)
print(reduce(lambda x, y: x*y, total_ways))