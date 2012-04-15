

for c in count:
	cp = 0.
	for note in count[c]:
		count[c][note] = count[c][note]/count[c]['sum'] + cp
		cp = count[c][note]
