import random

def write(p):

	# Position in measure
	l = 0

	# Initalize measure
	m = stream.Measure()

	# For each possible position in measure
	while l < 4:
		
		# Create note with p pitch and quarter duration
		n = note.Note(p)
		# n = pitch.pitchClass(p)
		n.duration.type = 'quarter'

		# Add this onto the measure
		m.append(n)

		# Change p based on probability matrix
		# Right now just going to highest probable following note
		
		r = random.random()
		print r

		if r <= count[p]['C']:
			p = 'C'
		elif r > count[p]['C'] and r <= count[p]['C#']:
			p = 'C#'
		elif r > count[p]['C#'] and r <= count[p]['D']:
			p = 'D'
		elif r > count[p]['E-'] and r <= count[p]['E']:
			p = 'E-'
		elif r > count[p]['E'] and r <= count[p]['F']:
			p = 'E'
		elif r > count[p]['F'] and r <= count[p]['F#']:
			p = 'F'
		elif r > count[p]['F#'] and r <= count[p]['G']:
			p = 'F#'
		elif r > count[p]['G'] and r <= count[p]['G#']:
			p = 'G'
		elif r > count[p]['G#'] and r <= count[p]['A']:
			p = 'G#'
		elif r > count[p]['A'] and r <= count[p]['B-']:
			p = 'A'
		elif r > count[p]['B-'] and r <= count[p]['B']:
			p = 'B-'
		else:
			p = 'B'

		print p
		l += 1

	song.append(m)