####################### COMPILATION.PY #########################

#!/usr/bin/python

# Compilation
# CS51 Final Project 2012

from music21 import *

# Import from files
import array1
import compare_pitch
import compare_duration 
import write_duration
import random

# Initialize counter variables
i = 0
j = 0
co = 0
k = 0
p = 0
cod = 0
d = 3

# Initialize song
song = music21.stream.Part()

# execfile('array.py')
# execfile('compare.py')
# execfile('write.py')

# Initialize notes and count
notes = {}
countn = {}
countd = {}

# Create an array of note sequences for each song
while i < 60:
	if (i == 33) or (i == 34):
		i += 1
	else:
		array1.array(i, notes)
		i += 1

# Map note transitions for all songs
while j < 60:
	if (j == 32) or (j == 33) or (j == 34):
		j += 1
	else:
		compare_pitch.compare(j, countn, notes)
		compare_duration.compare(j, countd, notes)
		j += 1

# Generate probability matrix for notes
while co < 12:
	compare_pitch.probability(co,countn)
	co += 1
	
while cod < 5:
	compare_duration.probability(cod, countd)
	cod += 1
	
# Combine pitch transition matrix with duration transition matrix to create a song
# dependent on two Markov models, pitch and duration

# Write 60 measures of song
while k < 60:
	write_duration.write(p, d, countn, countd, song)
	k+=1

# Display song as musicXML
song.show()

