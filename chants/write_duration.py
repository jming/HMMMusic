####################### WRITE.PY #########################

# Generates music file based on most probable path
# Current implementation works for order of 2

import random
import music21

noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']
dList = ['32nd', '16th', 'eighth', 'quarter', 'half', 'whole']

def write(p, d, countn, countd, song):

	# Position in measure
	l = 0

	# Initalize measure
	m = music21.stream.Measure()

	# For each possible position in measure
	while l < 4:
		
		# Change from number to pitch
		pit = noteList[p]
		# Change from number to duration type
		dur = dList[d]

		# Create note with p pitch and dur duration
		n = music21.note.Note(pit)
		# n = pitch.pitchClass(p)
		n.duration.type = dur

		# Add this onto the measure
		m.append(n)

		# Change p based on probability matrix for pitch
		r = random.random()
		# print r

		# Accounts for various cases for probabilty matrix
		# Should abstract this at some point
		if r <= countn[p][0]:
			p = 0
		elif r > countn[p][0] and r <= countn[p][1]:
			p = 1
		elif r > countn[p][1] and r <= countn[p][2]:
			p = 2
		elif r > countn[p][2] and r <= countn[p][3]:
			p = 3
		elif r > countn[p][3] and r <= countn[p][4]:
			p = 4
		elif r > countn[p][4] and r <= countn[p][5]:
			p = 5
		elif r > countn[p][5] and r <= countn[p][6]:
			p = 6
		elif r > countn[p][6] and r <= countn[p][7]:
			p = 7
		elif r > countn[p][7] and r <= countn[p][8]:
			p = 8
		elif r > countn[p][8] and r <= countn[p][9]:
			p = 9
		elif r > countn[p][9] and r <= countn[p][10]:
			p = 10
		else:
			p = 11
		
		# Change d based on probability matrix for duration
		r2 = random.random()
		# print r
		#'32nd','16th', 'eighth', 'quarter', 'half', 'whole'
		
		if r2 <= countd[d][0]:
			d = 0
			#d = '32nd'
		elif r2 > countd[d][0] and r2 <= countd[d][1]:
			d = 1
			#d = '16th'
		elif r2 > countd[d][1] and r2 <= countd[d][2]:
			d = 2
			#d = 'eighth'
		elif r2 > countd[d][2] and r2 <= countd[d][3]:
			d = 3
			#d = 'quarter'
		elif r2 > countd[d][3] and r2 <= countd[d][4]:
			d = 4
			#d = 'half'
		else:
			d = 5
			#d = 'whole'
			
		# Move ahead in measure
		l += 1

	song.append(m)
