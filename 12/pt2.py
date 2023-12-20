import re
filename = "input.txt"
# filename = "example.txt"

packs = {}
VERBOSE=False
def count_arrangements(springs, sig):
	def cache(res):
		packs[(springs, sig)] = res
	if((springs, sig) in packs): return packs[(springs, sig)]

	if(len(sig) == 0):
		cache("#" not in springs)
		if(VERBOSE): print("NOTHING TO PLACE: ", springs, sig, ("#" not in springs))
		return "#" not in springs
	first_group = sig[0]
	if len(springs) - sum(sig) - (len(sig)-1) < 0:
		cache(0)
		if(VERBOSE): print("NO FIT: ", springs, sig, 0)
		return 0
	holes = "." in springs[:first_group]
	if len(springs) == first_group:
		cache(0 if holes else 1)
		if(VERBOSE): print("SAME LENGTH", springs, sig, 0 if holes else 1)
		return 0 if holes else 1
	usable = not holes and springs[first_group]!="#"
	if(springs[0] == "#"):
		if usable:
			res = count_arrangements(springs[first_group+1:].lstrip("."), sig[1:])
			if(VERBOSE): print("# AT START: ", springs, sig, res)
			cache(res)
			return res
		else:
			cache(0)
			if(VERBOSE): print("# AT START BUT NO FIT: ", springs, sig, 0)
			return 0
	skip_res = count_arrangements(springs[1:].lstrip("."), sig)
	if not usable:
		cache(skip_res)
		if(VERBOSE): print("UNUSABLE STEP FWD: ", springs, sig, skip_res)
		return skip_res
	used_res = count_arrangements(springs[first_group+1:].lstrip("."), sig[1:])
	cache(skip_res+used_res)
	if(VERBOSE): print("SPLIT: ", springs, sig, skip_res+used_res)
	return skip_res+used_res

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		springs, sig = line.split(" ")
		springs = (springs+"?")*5
		springs = springs[:-1]
		springs = springs.lstrip(".")
		sig=[int(x) for x in sig.split(",")]
		sig = sig*5
		if(VERBOSE): print("######################")
		if(VERBOSE): print(springs,sig)
		total+=count_arrangements(springs, tuple(sig))
		line = f.readline().strip()
print(total)