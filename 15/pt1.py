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

print(sum([hash(x) for x in line.split(",")]))