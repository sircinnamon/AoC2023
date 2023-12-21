filename = "input.txt"
# filename = "example.txt"

grid = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(line)
		line = f.readline().strip()

slices_n = []
slices_w = []
slices_s = []
slices_e = []
rocks = {}
for x in range(len(grid[0])):
	for y in range(len(grid)):
		if y == 0:
			slices_n.append([])
		if(grid[y][x]=="#"):			
			slices_n.append([])
		else: slices_n[-1].append((x,y))

slices_n = list(filter(lambda x: len(x)!=0, slices_n))
slices_s = [x[::-1] for x in slices_n]

for y in range(len(grid)):
	for x in range(len(grid[y])):
		if x == 0:
			slices_w.append([])
		if(grid[y][x]=="#"):			
			slices_w.append([])
		else: slices_w[-1].append((x,y))

slices_w = list(filter(lambda x: len(x)!=0, slices_w))
slices_e = [x[::-1] for x in slices_w]

# Generate a dict of rocks
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == "O":
			rocks[(x,y)] = 1
		else: rocks[(x,y)] = 0

def shift_section(section, rocks):
	count = 0
	for k in section:
		if(rocks[k]):
			count+=1
			rocks[k]=0
	for i in range(count):
		rocks[section[i]] = 1

def spin_cycle(rocks):
	for n in slices_n:
		shift_section(n, rocks)
	for w in slices_w:
		shift_section(w, rocks)
	for s in slices_s:
		shift_section(s, rocks)
	for e in slices_e:
		shift_section(e, rocks)

def state(rocks):
	out = []
	for r in rocks.keys():
		if(rocks[r]):
			out.append(r)
	return out

		

# spin_cycle(rocks)
history = [state(rocks)]
while True:
	spin_cycle(rocks)
	s = state(rocks)
	if(s in history):
		# we are looping
		# print("BREAK ON ", len(history))
		break
	history.append(s)

target_cycle_count = 1000000000
loop_start = history.index(s)
loop_len = len(history)-loop_start
# Position in cycle at target_cycle_count
cycles = (target_cycle_count - loop_start) % loop_len
load = 0
for r in history[loop_start+cycles]:
	load+=(len(grid)-r[1])
print(load)