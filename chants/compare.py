# Assoc array within assoc array of frequency of note combinations
# Current implementation accounts for order of 2
# Works for all except 32.mid (excluded)

# countmatrix = [[0]*12]*12

# n = 0
# m = 0

# count = [[0]*12]*12

# for n in (0,11):
# 	for m in (0,11):
# 		count[n][m] = 0

def compare( j, count, notes ):
	
	# Specific note matrix from file
	notey = notes[j]

	# Length of note matrix
	length = len(notey)

	# Position in note matrix
	x = 0

	# Loop through each note in matrix
	while x < length - 1:

		# Establish pitch names
		a = notey[x].pitch.name
		b = notey[x+1].pitch.name

		# Increase count of specific note pair in array
		if a in count:
			if b in count[a]:
				count[a][b] += 1.
			else:
				count[a][b] = 1.
		else:
			count[a] = {}
			count[a][b] = 1.

		# Increase the sum
		if 'sum' in count[a]:
			count[a]['sum'] += 1.
		else:
			count[a]['sum'] = 1.

		x += 1

	# Go through and change everything into comparative
	for co in count:

		# Initialize cumulative probability
		cp = 0.

		# Go through each note in the count
		for c in count[co]:

			# Divide by total and add cumulative probability
			count[co][c] = count[co][c]/count[co]['sum'] + cp

			# Change cumulative probability to reflect difference
			cp = count[co][c]
