

noteList = ['A','A#','B','B#','C','C#','D','D#','E','E#','F#','G','G#']

matrix = []
inside = []

n = 0
m = 0

while n < 16:
	inside.append(0)
	n += 1

while n < 16:
	matrixy[n] = []

while n < 16:
	while m < 16:
		matrix[n][m]=0

for note in noteList:
	matrix[note] = {}
	
for note in noteList:
	for n in noteList:
		matrix[note][n] = 0

for c in count
	for 