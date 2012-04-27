####################### COMPILATION3.PY #########################

#!/usr/bin/python

# Compilation using 3 note chains
# CS51 Final Project 2012

from music21 import *

# Import from files
import array
import compare 
import write
import random
import compare3
import diatonichwrite3
import compare

# Initialize counter variables
i = 0
j = 0
c2 = 0
co = 0
co2 = 0
k = 0


# Initialize song
song = stream.Part()


# Initialize notes and count
notes = {}
count2 = {}
count3 = {}

# Create an array of note sequences for each song
while i < 60:
        if (i == 33) or (i == 34):
                i += 1
        else:
                array.array(i, notes)
                i += 1

# Map both order 2 and order 3 note transitions for all songs
while j < 60:
        if (j == 32) or (j == 33) or (j == 34):
                j += 1
        else:
                compare.compare(j, count2, notes)
                compare3.compare(j, count3, notes)
                j += 1

# Generate probability matrix
while co < 12:
        while co2 < 12:
                compare.probability(c2, count2)
                compare3.probability(co, co2, count3)
                co2 += 1
        co += 1
        co2 = 0

# Write 60 measures of song
diatonichwrite3.writer(count2, count3, song, 60)

# Display song as musicXML
song.show()

