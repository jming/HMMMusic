######################## ARRAY.PY #########################
#                 CS51 Final Project 2012                 #
########### Alisa Nguyen, Joy Ming, Lee Seligman ##########
                                            
# Create associative array of all pitches in each midi    #
# This works for all files except 35.mid                  #

from music21 import *

# Initialize associative array
notes = {}

# Appends for given file i
def appendNote(i):
	
	# Initialize array for key i
	notes[i] = []
	# Parse file given music21 function
	s = converter.parse('%i.mid' % (i))
	# Access measures for file
	measures = s[0].measures(1,60)

	# Loop through each measure
	for measure in measures:
		# Add each note to the array at key i
		for note in measure.notes:
			notes[i].append(note)

# Loops through all 60 files
while i < 60:
	appendNote(i)
	i += 1