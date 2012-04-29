####################### COMPARE.PY #########################
# CS51 Final Project

# Assoc array within assoc array of frequency of note combinations
# Current implementation accountds for order of 2
# Works for all except 32.mid (excluded)
import music21

def compare( j, countd, notes ):
	
	# Specific note matrix from file
	notey = notes[j]

	# Position in note matrix
	x = 0

	# Array of duration sequence (rhythm) of song, in tuple type
	durations = []
	
	# Establishes note durations as closest duration type to numerical representation
	# i.e. '16th', 'eighth', 'quarter', 'half', 'whole'
	for n in notey:
		durations.append(music21.duration.quarterLengthToClosestType(n.duration.quarterLength))
	
	# Array of duration sequence of song with only duration types
	durations2 = []
	
	# Duration types returned as tuple, detuples and adds them to a list, filtering out
	# unnecessary information
	for d in durations:
		for e in d:
			if isinstance(e, str):
				durations2.append(e)

				
	
	#PROBABLY NOT NEEDED
	durations3 = []
	# Converts duration type names of notes into numbers for easy manipulation
	# Assigns integer values to each note duration type
	for y in durations2:
		if y =='16th':
			durations3.append(0)
		elif y == 'eighth': 
			durations3.append(1)
		elif y == 'quarter': 
			durations3.append(2)
		elif y =='half': 
			durations3.append(3)
		elif y =='whole': 
			durations3.append(4)
	
	
	# length of durations2
	length = len(durations3)
	
	# Loop through each note in matrix
	while x < length - 1:
		
		a = durations3[x]
		b = durations3[x+1]
		
		# Increase countd of specific note pair in array
		if a in countd:
			if b in countd[a]:
				countd[a][b] += 1.
			else:
				countd[a][b] = 1.
		else:
			countd[a] = {}
			countd[a][b] = 1.

		# Increase the sum
		if 'sum' in countd[a]:
			countd[a]['sum'] += 1.
		else:
			countd[a]['sum'] = 1.

		x += 1

# Change to probability matrix as opposed to simple countd

def probability (cod, countd):

	# # Go through and change everything into comparative
		# Initialize cumulative probability
	cp = 0.
	c = 0

		# Go through each note in the countd
	while c < 5:

			# Divide by total and add cumulative probability
		if c in countd[cod]:
			countd[cod][c] = countd[cod][c]/countd[cod]['sum'] + cp
		else:
			countd[cod][c] = 0. + cp

			# Change cumulative probability to reflect difference
		cp = countd[cod][c]
		c += 1

		#cod += 1
