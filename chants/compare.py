# Assoc array within assoc array of frequency of note combinations
# Current implementation accounts for order of 2
# Works for all except 32.mid (excluded)

def compare( j, count, notes ):
	
	# Specific note matrix from file
	note = notes[j]

	# Length of note matrix
	length = len(note)

	# Position in note matrix
	x = 0

	# Loop through each note in matrix
	while x < length - 1:

		# Establish pitch names
		a = note[x].pitchClass
		b = note[x+1].pitchClass

		# Increase count of specific note pair in array
		if a in count:
			if b in count[a]:
				count[a][b] = count[a][b] + 1
			else:
				count[a][b] = 1
		else:
			count[a] = {}
			count[a][b] = 1
		x += 1