####################### COMPARE3.PY #########################
# CS51 Final Project

# Assoc array within assoc array of frequency of note combinations
# This implementation accounts for three-note sequences
# Works for all except 32.mid (excluded)

def compare( j, count, notes ):
	
	# Specific note matrix from file
	notey = notes[j]

	# Length of note matrix
	length = len(notey)

	# Position in note matrix
	x = 0

	# Loop through each note in matrix
	while x < length - 3:

		# Establish pitch names
		a = notey[x].pitchClass
		b = notey[x+1].pitchClass
		c = notey[x+2].pitchClass


		# Increase count of specific note triplet in array
		if a in count:
			if b in count[a]:
                if c in count[a][b]:
                        count[a][b][c] += 1
                else:
                        count[a][b][c] = 1.
			else:
				count[a][b] = {}
				count[a][b][c] = 1.
		else:
			count[a] = {}
			count[a][b] = {}
			count[a][b][c] = 1.


		# Increase the sum
		if 'sum' in count[a][b]:
			count[a][b]['sum'] += 1.
		else:
			count[a][b]['sum'] = 1.
                        
		x += 1

# Change to probability matrix as opposed to simple count

def probability (co,co2, count):

	# Go through and change everything into comparative
        #co2 = 0
        #while co2 < 12:

        #check whether this state exists in "count"
        if co2 in count[co]:

                # Initialize cumulative probability
                cp = 0.
                i = 0

                # Go through each note in the count
                while i < 12:

                        # Divide by total and add cumulative probability
                        if i in count[co][co2]:
                                count[co][co2][i] = count[co][co2][i]/count[co][co2]['sum'] + cp
                        else:
                                count[co][co2][i] = 0. + cp

                        # Change cumulative probability to reflect difference
                        cp = count[co][co2][i]
                        i += 1
                #co2 += 1
        
        else:
                return
                #co2 += 1

