####################### ARRAY.PY #########################

# Associative array of all pitches in each midi
# Works for all files except 35.mid (excluded)

import music21

def array( i, notes ):

	# Initialize array for key i
	notes[i] = []
	# Parse file given using music21 function
	s = music21.converter.parse('%i.mid' % (i))
	# Access measures for file
	measures = s[0].measures(1,60)

	# Loop through each measure
	for measure in measures:
		# Add each note to the array at key i
		for notey in measure.notes:
			notes[i].append(notey)