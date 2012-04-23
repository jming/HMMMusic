####################### COMPILATION3.PY #########################

#!/usr/bin/python

# Compilation using 3 note chains
# CS51 Final Project 2012

from music21 import *

# Import from files
import array1
import compare 
import write
import random
import compare3

# Initialize counter variables
i = 0
j = 0
co = 0
k = 0
p1 = random.randint(0,11)
p2 = random.randint(0,11)

# Initialize song
song = stream.Part()

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
		array1.array(i, notes)
		i += 1

# Map note transitions for all songs
while j < 60:
	if (j == 32) or (j == 33) or (j == 34):
		j += 1
	else:
		compare3.compare(j, count, notes)
		j += 1

# Generate probability matrix
while co < 12:
	compare3.probability(co,count)
	co += 1

# Write 60 measures of song
while k < 60:
        if k == 0:
            write3.writefirst(p1, p2, count, song)
            k+=1 
        else:    
            write3.write(p1, p2, count, song)
            k+=1

# Display song as musicXML
song.show()

