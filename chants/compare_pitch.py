####################### COMPARE.PY #########################
# CS51 Final Project

# Assoc array within assoc array of frequency of note combinations
# Current implementation accounts for order of 2
# Works for all except 32.mid (excluded)
import music21

def compare( j, countn, notes):
	
	# Specific note matrix from file
	notey = notes[j]

	# Length of note matrix
	length = len(notey)

	# Position in note matrix
	x = 0

	# Loop through each note in matrix
	while x < length - 1:

		# Establish pitch names
		a = notey[x].pitchClass
		b = notey[x+1].pitchClass

		# Increase count of specific note pair in array
		if a in countn:
			if b in countn[a]:
				countn[a][b] += 1.
			else:
				countn[a][b] = 1.
		else:
			countn[a] = {}
			countn[a][b] = 1.

		# Increase the sum
		if 'sum' in countn[a]:
			countn[a]['sum'] += 1.
		else:
			countn[a]['sum'] = 1.

		x += 1

# Change to probability matrix as opposed to simple count

def probability (co,countn):

	# # Go through and change everything into comparative
	# while co < 12:

		# Initialize cumulative probability
		cp = 0.
		c = 0

		# Go through each note in the count
		while c < 12:

			# Divide by total and add cumulative probability
			if c in countn[co]:
				countn[co][c] = countn[co][c]/countn[co]['sum'] + cp
			else:
				countn[co][c] = 0. + cp

			# Change cumulative probability to reflect difference
			cp = countn[co][c]
			c += 1

		# co += 1
