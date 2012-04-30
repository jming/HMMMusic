####################### COMPILATION.PY #########################
#
# Alisa Nguyen, Lee Seligman, Joy Ming
# CS 51 Final Project Spring 2012
# Mirroring Music: Music Generation with Hidden Markov Models
#
#!/usr/bin/python
#
# Compilation generates a random song based on an Order 2
# pitch Markov model 
#
####################### COMPILATION.PY #########################

from music21 import *

# Import from files
import notearray
import compare 
import write
import random

# Initialize counter variables
i = 0
j = 0
co = 0
k = 0
p = 0

# Initialize song
song = music21.stream.Part()

# execfile('array.py')
# execfile('compare.py')
# execfile('write.py')

# Initialize notes and count
notes = {}
count = {}

# Create an array of note sequences for each song
while i < 60:
	if (i == 33) or (i == 34):
		i += 1
	else:
		notearray.array(i, notes)
		i += 1

# Map note transitions for all songs
while j < 60:
	if (j == 32) or (j == 33) or (j == 34):
		j += 1
	else:
		compare.compare(j, count, notes)
		j += 1

# Generate probability matrix
while co < 12:
	compare.probability(co,count)
	co += 1

# Write 60 measures of song
while k < 60:
	write.write(p, count, song)
	k+=1

# Display song as musicXML
song.show()

