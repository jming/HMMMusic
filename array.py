# This file helps to create arrays of all the notes in each midi file

# Initializes associative arrays for notes

notes = {}
def appendNote(i):
	s = converter.parse('%i.mid' % (i))
	notes[i] = []
	measures = s[0].measures(1,60)
	for measure in measures:
		for note in measure.notes:
			notes[i].append(note)

pitches = {}
def appendPitch(i):
	s = converter.parse('%i.mid' % (i))
	pitches[i] = []
	measures = s[0].measures(1,60)
	for measure in measures:
		for note in measure.notes:
			pitches[i].append(note.pitch)

while i < 60: 

	append(i)
	i += 1

	# Converts the specific midi file
	s = converter.parse('%i.mid' % (i))
	# Initializes notes for that index
	notes[i] = []

	measures = s[0].measures(1,60)

	for measure in measures:
		for note in measure.notes:
			notes[i].append(note.pitch)

	i += 1