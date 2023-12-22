from collections import deque

filename = "input.txt"
# filename = "example.txt"

line = ""
with open(filename, "r") as f:
	line = f.readline().strip()

def hash(v):
	val = 0
	for c in v:
		val = ((val+ord(c))*17)%256
	return val

boxes = [[] for i in range(256)]
def remove_from_box(label, boxid):
	boxes[boxid] = deque(list(filter(lambda x: x != None and x[0] != label, boxes[boxid])))

def add_to_box(label, boxid, lens):
	box = list(boxes[boxid])
	for i,l in enumerate(box):
		if l[0] == lens[0]:
			box[i] = lens
			boxes[boxid] = box
			return
	box.append(lens)
	boxes[boxid] = box

for instr in line.split(","):
	if "-" in instr:
		label = instr[:-1]
		box = hash(label)
		remove_from_box(label, box)
	else:
		label, val = instr.split("=")
		val = int(val)
		box = hash(label)
		add_to_box(label, box, (label, val))

total = 0
for i,b in enumerate(boxes):
	b_total = 0
	for j,l in enumerate(b):
		b_total += (i+1)*(j+1)*l[1]
	total += b_total
print(total)
