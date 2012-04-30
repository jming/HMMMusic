####################### WRITE.PY ############################
#
# Alisa Nguyen, Lee Seligman, Joy Ming
# CS 51 Final Project Spring 2012
# Mirroring Music: Music Generation with Hidden Markov Models
#
# Generates music file based on most probable path
# Current implementation works for order of 2
#
####################### WRITE.PY ############################

import random
import music21

# Array of all possible notes
noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']

def write(p, count, song):

	# Position in measure
	l = 0

	# Initalize measure
	m = music21.stream.Measure()

	# For each possible position in measure
	while l < 4:
		
		# Change from number to pitch
		pit = noteList[p]

		# Create note with p pitch and quarter duration
		n = music21.note.Note(pit)
		# n = pitch.pitchClass(p)
		n.duration.type = 'quarter'

		# Add this onto the measure
		m.append(n)

		# Change p based on probability matrix
		r = random.random()
		# print r

		# Accounts for various cases for probabilty matrix
		# Should abstract this at some point
		if r <= count[p][0]:
			p = 0
		elif r > count[p][0] and r <= count[p][1]:
			p = 1
		elif r > count[p][1] and r <= count[p][2]:
			p = 2
		elif r > count[p][2] and r <= count[p][3]:
			p = 3
		elif r > count[p][3] and r <= count[p][4]:
			p = 4
		elif r > count[p][4] and r <= count[p][5]:
			p = 5
		elif r > count[p][5] and r <= count[p][6]:
			p = 6
		elif r > count[p][6] and r <= count[p][7]:
			p = 7
		elif r > count[p][7] and r <= count[p][8]:
			p = 8
		elif r > count[p][8] and r <= count[p][9]:
			p = 9
		elif r > count[p][9] and r <= count[p][10]:
			p = 10
		else:
			p = 11

		# Move ahead in measure
		l += 1

	song.append(m)
