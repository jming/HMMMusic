######################## WRITE.PY ########################

p = 'C'
song = stream.Part()

i = 1
while i < 5:
	j = 0
	m = stream.Measure()
	while j < 4:
		n = note.Note(p)
		n.duration.type = 'quarter'
		m.append(n)
		p = count[p].keys()[0]
		j += 1
	song.append(m)
	i += 1

song.show()

