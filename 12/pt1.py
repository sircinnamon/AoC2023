import re
filename = "input.txt"
# filename = "example.txt"

def clean_row(springs, sig):
	# remove "solved" ends
	while(m:=re.match("^\\.*#+\\.", springs)):
		# print(m, m.end())
		springs = springs[m.end():]
		sig = sig[1:]
		# print("A", springs, sig)
	while(m:=re.match(".*(\\.#+\\.*)$", springs)):
		# print(m, m.start(1))
		springs = springs[:m.start(1)]
		sig = sig[:-1]
		# print(springs, sig)
	return [springs, sig]


def count_arrangements(springs, sig):
	used = springs.count("#")
	needed = sum(sig)
	possibles = springs.count("?")
	if(used>=needed):
		springs = springs.replace("?",".")
		if(validate_arrangement(springs, sig)):
			print(springs,sig,"VALID")
			return 1
		else:
			# print(springs,sig,"INVALID")
			return 0
	if(possibles <(needed-used)):
		return 0
	next_q = springs.find("?")
	total = 0
	springs = springs[:next_q]+"#"+springs[next_q+1:]
	total+=count_arrangements(springs,sig)
	springs = springs[:next_q]+"."+springs[next_q+1:]
	total+=count_arrangements(springs,sig)
	return total

def validate_arrangement(springs, sig):
	constructed_re = "^\\.*"
	for chunk in sig:
		constructed_re+="#{{{}}}\\.+".format(chunk)
	constructed_re = constructed_re[:-1]+"*$"
	return re.match(constructed_re, springs) != None

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		springs, sig = line.split(" ")
		sig=[int(x) for x in sig.split(",")]
		springs, sig = clean_row(springs, sig)
		# print("######################")
		# print(springs,sig)
		# print(count_arrangements(springs,sig))
		total+=count_arrangements(springs, sig)
		line = f.readline().strip()
print(total)