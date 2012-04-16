from music21 import *

def array(i):
	notes[i] = []
	s = converter.parse('%i.mid' % (i))
	measures = s[0].measures(1,60)
	for measure in measures:
		for note in measure.notes:
			notes[i].append(note)


def compare(j):
	note = notes[j]
	length = len(note)
	x = 0
	while x < length - 1:
		a = note[x].pitch.name
		b = note[x+1].pitch.name
		if a in count:
			if b in count[a]:
				count[a][b] = count[a][b] + 1
			else:
				count[a][b] = 1
		else:
			count[a] = {}
			count[a][b] = 1
		x += 1

def optimize():
	for c in count:
		comp = ('',0)
		for note in count[c]:
			if note != c:
				if comp[1] < count[c][note]:
					comp = (note, count[c][note])
		count[c] = {comp[0]:comp[1]}

def write():
	l = 0
	m = stream.Measure()
	while l < 4:
		n = note.Note(p)
		n.duration.type = 'quarter'
		m.append(n)
		p = count[p].keys()[0]
		j += 1
	song.append(m)

i = 0
j = 0
k = 0

notes = {}
count = {}
song = stream.Part()

p = 'C'
song_length = 60

# Create an array of note sequences for each song
while i < 60:
	array(i)
	i += 1
