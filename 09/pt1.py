filename = "input.txt"
# filename = "example.txt"

def predict_next(seq):
	if(len(set(seq)) == 1): return seq[0]
	deriv = []
	for i,x in enumerate(seq[1:]):
		# print(x, seq[i])
		deriv.append(x-seq[i])
	nxt = predict_next(deriv)+seq[-1]
	# print(seq, nxt)
	return nxt

total = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		seq = [int(x) for x in line.split(" ")]
		total+=predict_next(seq)
		line = f.readline().strip()
print(total)