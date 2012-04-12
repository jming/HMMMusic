

noteList = ['A','B','C','D','E','F','G','A#','B#','C#','D#','E#','F#','G#']

matrix = {}

for note in noteList:
	matrix[note] = {}
	
for note in noteList:
	for n in noteList:
		matrix[note][n] = 0

