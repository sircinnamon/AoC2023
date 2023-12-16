import re
filename = "input.txt"
# filename = "example.txt"

def determine_type(hand):
	hand = list(hand)
	hand.sort()
	hand = ''.join(hand)
	# print(hand)
	if(re.fullmatch("(.)\\1{4}", hand)): return "FIVE_KIND"
	if(re.search("(.)\\1{3}", hand)): return "FOUR_KIND"
	if(re.fullmatch("(.)\\1\\1(.)\\2", hand)): return "FULL_HOUSE"
	if(re.fullmatch("(.)\\1(.)\\2\\2", hand)): return "FULL_HOUSE"
	if(re.search("(.)\\1\\1", hand)): return "THREE_KIND"
	if(re.fullmatch(".?(.)\\1.?(.)\\2.?", hand)): return "TWO_PAIR"
	if(re.search("(.)\\1", hand)): return "PAIR"
	return "HIGH_CARD"

def score_hand(hand):
	BASE = 10000000000
	HIGH_CARD  = BASE*1
	PAIR       = BASE*2
	TWO_PAIR   = BASE*3
	THREE_KIND = BASE*4
	FULL_HOUSE = BASE*5
	FOUR_KIND  = BASE*6
	FIVE_KIND  = BASE*7
	value = "23456789TJQKA"
	typ = determine_type(hand)
	# print(hand, typ)
	score = 0
	if(typ == "HIGH_CARD"): score += HIGH_CARD
	elif(typ == "PAIR"): score += PAIR
	elif(typ == "TWO_PAIR"): score += TWO_PAIR
	elif(typ == "THREE_KIND"): score += THREE_KIND
	elif(typ == "FULL_HOUSE"): score += FULL_HOUSE
	elif(typ == "FOUR_KIND"): score += FOUR_KIND
	elif(typ == "FIVE_KIND"): score += FIVE_KIND
	for i,c in enumerate(hand):
		score += value.index(c) * 100**(4-i)
	return score

hands = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		hand, bid = line.split(" ")
		hands.append([hand, int(bid), 0])
		line = f.readline().strip()

for hand in hands:
	hand[2] = score_hand(hand[0])
hands.sort(key=lambda x: x[2])

# print(hands)

total = 0
for i,hand in enumerate(hands):
	total+= (i+1)*hand[1]
print(total)