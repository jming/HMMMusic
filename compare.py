######################## COMPARE.PY ########################
#                 CS51 Final Project 2012                  #
########### Alisa Nguyen, Joy Ming, Lee Seligman ###########

# Keeps track of each note combination
# Starts with order of 2
# This works for all except 32.mid

# Array of counts
count = {}

# File number
i = 0

# Loop through each file
while i < 60: 

	# Initialize variables
	note = notes[i]
	length = len(note)
	# Note position in array
	x = 0

	# Loop through each note
	while x < length - 1: 
		# establish pitch names
		a = note[x].pitch.name
		b = note[x+1].pitch.name

		# Store as pair in array
		if a in count:
			if b in count[a]:
				count[a][b] = count[a][b] + 1
			else:
				count[a][b] = 1
		else:
			count[a] = {}
			count[a][b] = 1
		x += 1

	i += 1

*************

while i < 60:
	note = notes[i]
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
		x+=1
	i+=1

