#!/usr/bin/python

# Compilation
# CS51 Final Project 2012

from music21 import *

################## FUNCTION DEFINITIONS ##################

# Associative array of all pitches in each midi
# Works for all files except 35.mid (excluded)

def array(i):

	# Initialize array for key i
	notes[i] = []
	# Parse file given using music21 function
	s = converter.parse('%i.mid' % (i))
	# Access measures for file
	measures = s[0].measures(1,60)

	# Loop through each measure
	for measure in measures:
		# Add each note to the array at key i
		for note in measure.notes:
			notes[i].append(note)

# Assoc array within assoc array of frequency of note combinations
# Current implementation accounts for order of 2
# Works for all except 32.mid (excluded)

def compare(j):
	
	# Specific note matrix from file
	note = notes[j]

	# Length of note matrix
	length = len(note)

	# Position in note matrix
	x = 0

	# Loop through each note in matrix
	while x < length - 1:

		# Establish pitch names
		a = note[x].pitch.name
		b = note[x+1].pitch.name

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

# Determines most probable path from one note to another
# Current implementation works for order of 2

def optimize():

	# For each beginning note
	for c in count:

		# Stores highest frequency following note
		comp = ('',0)

		# Loop through each 
		for note in count[c]:
			# Strip same note combinations
			# Where beginning note = following note
			if note != c:
				# Store in comp higher frequency following note
				if comp[1] < count[c][note]:
					comp = (note, count[c][note])

		# Store this as count instead
		count[c] = {comp[0]:comp[1]}

# Generates music file based on most probable path
# Current implementation works for order of 2

def write():

	# Position in measure
	l = 0

	# Initalize measure
	m = stream.Measure()

	# For each possible position in measure
	while l < 4:
		
		# Create note with p pitch and quarter duration
		n = note.Note(p)
		n.duration.type = 'quarter'

		# Add this onto the measure
		m.append(n)

		# Change p based on probability matrix
		# Right now just going to highest probable following note
		p = count[p].keys()[0]

		j += 1

	song.append(m)

################## INITIALIZE VARIABLES ##################

# Various counters for implementation
i = 0
j = 0
k = 0

# Various arrays for information storage
notes = {}
count = {}
song = stream.Part()

# Starting pitch
p = 'C'

# Length of song
song_length = 60

################## IMPLEMENT FUNCTIONS ##################

# Create an array of note sequences for each song
while i < 60:
	array(i)
	i += 1

# Map probabilities of note transitions for all songs
while j < 60
	compare(j)
	j += 1

# Reduce probability matrix to only include most probable
optimize()

# Write a song of length song_length based on probability matrix
while k < song_length:
	write()
	k += 1

# Show MusicXML as readable format
song.show()

