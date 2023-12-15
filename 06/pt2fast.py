from functools import reduce
from math import floor
filename = "input.txt"
# filename = "example.txt"

def does_win(press_time, move_time, record):
	return ((press_time*move_time) > record)

times = []
dists = []
with open(filename, "r") as f:
	times = [int(x) for x in filter(lambda x: x!="", f.readline().strip().replace(" ","").split(":")[1].split(" "))	]
	dists = [int(x) for x in filter(lambda x: x!="", f.readline().strip().replace(" ","").split(":")[1].split(" "))]

# print(times)
# print(dists)
total_ways = []
for ri in range(len(times)):
	t = times[ri]
	rec = dists[ri]
	min_victory = t
	max_victory = 0
	center = round(t/2)
	i = 0
	jump_size = floor(t/4)
	while True:
		min_test = center - i
		max_test = center + i
		shrink = False
		if(min_test >= 0 and does_win(min_test, t-min_test, rec)):
			min_victory = min_test
		else:
			i -= jump_size
			shrink = True
		if(max_test < t and does_win(max_test, t-max_test, rec)):
			max_victory = max_test
		else:
			i -= jump_size
			shrink = True
		if(shrink):
			jump_size = floor(jump_size/2)
		if(jump_size==0):
			break
		i+=jump_size
	# print("Win race: hold for {} to {} ms".format(min_victory, max_victory))
	total_ways.append((max_victory-min_victory)+1)
# print(total_ways)
print(reduce(lambda x, y: x*y, total_ways))