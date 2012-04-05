# This file helps to create arrays of all the notes in each midi file

# Initializes associative arrays for notes
notes = {}
i = 0

while i < 60: 

	# Converts the specific midi file
	s = converter.parse('%i.mid' % (i))
	# Initializes notes for that index
	notes[i] = []

	measures = s[0].measures(1,60)

	for measure in measures:
		for note in measure.notes:
			notes[i].append(note.pitch)

	i += 1