####################### WRITE3.PY #########################

# Generates music file based on most probable path
# For 3-note chains, 4 quarter notes per measure

import random
import music21

noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']

def writefirst(p1, p2, count, song):

    # Initialize random number
    r = random.random()

    # Initialize measure
    m = music21.stream.Measure()

    # Choose a new second pitch if this is an uncommon combination
    # The number 3 is an arbitrary limit on how common a combination must be
    while count[p1][p2]['sum'] < 3:
        p2 = random.randint(0,11)
        
    # If combination sufficiently common, write to measure
    # First, create notes
    n1 = music21.note.Note(noteList[p1])
    n2 = music21.note.Note(noteList[p2])

    # Modify duration
    n1.duration.type = 'quarter'
    n2.duration.type = 'quarter'

    # Write to measure
    m.append(n1)
    m.append(n2)

    # Hold current p2 in a dummy variable
    currp2 = p2
    
    # Accounts for various cases for probabilty matrix
    if r <= count[p1][p2][0]:
	    p2 = 0
    elif r > count[p1][p2][0] and r <= count[p1][p2][1]:
	    p2 = 1
    elif r > count[p1][p2][1] and r <= count[p1][p2][2]:
	    p2 = 2
    elif r > count[p1][p2][2] and r <= count[p1][p2][3]:
            p2 = 3
    elif r > count[p1][p2][3] and r <= count[p1][p2][4]:
	    p2 = 4
    elif r > count[p1][p2][4] and r <= count[p1][p2][5]:
	    p2 = 5
    elif r > count[p1][p2][5] and r <= count[p1][p2][6]:
	    p2 = 6
    elif r > count[p1][p2][6] and r <= count[p1][p2][7]:
	    p2 = 7
    elif r > count[p1][p2][7] and r <= count[p1][p2][8]:
	    p2 = 8
    elif r > count[p1][p2][8] and r <= count[p1][p2][9]:
	    p2 = 9
    elif r > count[p1][p2][9] and r <= count[p1][p2][10]:
	    p2 = 10
    else:
	    p2 = 11


    # New p1 is now former p2
    p1 = currp2
    
    # Write two more notes in measure to make a four-note measure
    writepitch(p1, p2, count)
    writepitch(p1, p2, count)
    
    #write measure to song
    song.append(m)

    
def writepitch(p1,p2,count):
    # Change from number to pitch (will only need to write p2)
    pit2 = noteList[p2]

    # Create note with p2 pitch and quarter duration
    n2 = music21.note.Note(pit2)
    n2.duration.type = 'quarter'

    # Add this onto the measure
    m.append(n2)

    # Change p2 based on probability matrix
    r = random.random()

    # Hold current p2 in a dummy variable
    currp2 = p2
    
    # Accounts for various cases for probabilty matrix
    if r <= count[p1][p2][0]:
	    p2 = 0
    elif r > count[p1][p2][0] and r <= count[p1][p2][1]:
	    p2 = 1
    elif r > count[p1][p2][1] and r <= count[p1][p2][2]:
	    p2 = 2
    elif r > count[p1][p2][2] and r <= count[p1][p2][3]:
            p2 = 3
    elif r > count[p1][p2][3] and r <= count[p1][p2][4]:
	    p2 = 4
    elif r > count[p1][p2][4] and r <= count[p1][p2][5]:
	    p2 = 5
    elif r > count[p1][p2][5] and r <= count[p1][p2][6]:
	    p2 = 6
    elif r > count[p1][p2][6] and r <= count[p1][p2][7]:
	    p2 = 7
    elif r > count[p1][p2][7] and r <= count[p1][p2][8]:
	    p2 = 8
    elif r > count[p1][p2][8] and r <= count[p1][p2][9]:
	    p2 = 9
    elif r > count[p1][p2][9] and r <= count[p1][p2][10]:
	    p2 = 10
    else:
	    p2 = 11

    # New p1 is now former p2
    p1 = currp2


def write(p, count, song):

	# Position in measure
	l = 0

	# Initalize measure
	m = music21.stream.Measure()

	# For each possible position in measure
	while l < 4:
		
        #write a pitch for each space in the measure
            writepitch(p1, p2, count)
            l += 1

        #write measure to song
        song.append(m)
            
