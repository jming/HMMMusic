# Results in one path
for c in count:
	i = ('',0)
	for note in count[c]:
		# Strip same note combinations
		if note != c:
			if i[1] < count[c][note]:
				i = (note,count[c][note])
	count[c] = {i[0]:i[1]}
	
