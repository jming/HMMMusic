####################### WRITE3.PY ###########################
#
# Alisa Nguyen, Lee Seligman, Joy Ming
# CS 51 Final Project Spring 2012
# Mirroring Music: Music Generation with Hidden Markov Models
#
# Generates music file based on most probable path
# For 3-note chains, 4 quarter notes per measure
#
####################### WRITE3.PY ###########################

import random
import music21

noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']

def writefirst(pt1, pt2, count, song):

    global p1
    global p2
    
    # Initialize random number
    r = random.random()

    # Find a second note that can come after the first with some non-zero probability
    dummy = True
    while dummy:
        if pt1 not in count:
            pt1 = random.randint(0,11)
        elif pt2 not in count[pt1]:
            pt2 = random.randint(0,11)
        # The number 3 is an arbitrary limit on how common a two-note combination
        # must be
        elif count[pt1][pt2]['sum'] < 3:
            pt1 = random.randint(0,11)
            pt2 = random.randint(0,11)
        else:
            dummy = False
        
    # If combination sufficiently common, write to measure
    # First, create notes
    n1 = music21.note.Note(noteList[pt1])
    n2 = music21.note.Note(noteList[pt2])

    # Modify duration
    n1.duration.type = 'quarter'
    n2.duration.type = 'quarter'

    # Initialize measure 
    m = music21.stream.Measure()

    # Write to measure
    m.append(n1)
    m.append(n2)


    # Accounts for various cases for probabilty matrix
    if r <= count[pt1][pt2][0]:
	    p2 = 0
    elif r > count[pt1][pt2][0] and r <= count[pt1][pt2][1]:
	    p2 = 1
    elif r > count[pt1][pt2][1] and r <= count[pt1][pt2][2]:
	    p2 = 2
    elif r > count[pt1][pt2][2] and r <= count[pt1][pt2][3]:
            p2 = 3
    elif r > count[pt1][pt2][3] and r <= count[pt1][pt2][4]:
	    p2 = 4
    elif r > count[pt1][pt2][4] and r <= count[pt1][pt2][5]:
	    p2 = 5
    elif r > count[pt1][pt2][5] and r <= count[pt1][pt2][6]:
	    p2 = 6
    elif r > count[pt1][pt2][6] and r <= count[pt1][pt2][7]:
	    p2 = 7
    elif r > count[pt1][pt2][7] and r <= count[pt1][pt2][8]:
	    p2 = 8
    elif r > count[pt1][pt2][8] and r <= count[pt1][pt2][9]:
	    p2 = 9
    elif r > count[pt1][pt2][9] and r <= count[pt1][pt2][10]:
	    p2 = 10
    else:
	    p2 = 11


    # New p1 is now former p2
    p1 = pt2

    # Check to see that new p2 is found in transition matrix. Otherwise, find
    # a new random p2
    while count[p1][p2]['sum'] == 0:
        p2 = random.randint(0,11)
    
    # Write two more notes in measure to make a four-note measure
    writepitch(p1, p2, m, count)
    writepitch(p1, p2, m, count)

    #write measure to song
    song.append(m)

    print "End of writefirst, p1 = "
    print p1
    print "p2 ="
    print p2

    
def writepitch(no1,no2,measure,count):

    # Definition of global variables. pch1 and pch2 will only be used in
    # calls from write (as opposed to writefirst)
    global p1
    global p2
    global pch1
    global pch2
    global dummy1
    global dummy2

    #print "writepitch started with p1="
    #print p1
    #print "p2 = "
    #print p2
    #print "no1 = "
    #print no1
    #print "no2 = "
    #print no2

    # Change from number to pitch (will only need to write no)
    pit2 = noteList[p2]

    # Create note with p2 pitch and quarter duration
    n2 = music21.note.Note(pit2)
    n2.duration.type = 'quarter'

    # Add this onto the measure
    measure.append(n2)

    # Change p2 based on probability matrix
    r = random.random()
    
    # Accounts for various cases for probabilty matrix
    if r <= count[p1][p2][0]:
            p1 = p2
	    p2 = 0
	    dummy2 = 0
    elif r > count[p1][p2][0] and r <= count[p1][p2][1]:
            p1 = p2
	    p2 = 1
	    dummy2 = 1
    elif r > count[p1][p2][1] and r <= count[p1][p2][2]:
            p1 = p2
	    p2 = 2
	    dummy2 = 2
    elif r > count[p1][p2][2] and r <= count[p1][p2][3]:
            p1 = p2
            p2 = 3
            dummy2 = 3
    elif r > count[p1][p2][3] and r <= count[p1][p2][4]:
            p1 = p2
	    p2 = 4
	    dummy2 = 4
    elif r > count[p1][p2][4] and r <= count[p1][p2][5]:
            p1 = p2
	    p2 = 5
	    dummy2 = 5
    elif r > count[p1][p2][5] and r <= count[p1][p2][6]:
            p1 = p2
	    p2 = 6
            dummy2 = 6
    elif r > count[p1][p2][6] and r <= count[p1][p2][7]:
            p1 = p2
	    p2 = 7
	    dummy2 = 7
    elif r > count[p1][p2][7] and r <= count[p1][p2][8]:
            p1 = p2
	    p2 = 8
	    dummy2 = 8
    elif r > count[p1][p2][8] and r <= count[p1][p2][9]:
            p1 = p2
	    p2 = 9
	    dummy2 = 9
    elif r > count[p1][p2][9] and r <= count[p1][p2][10]:
            p1 = p2
	    p2 = 10
	    dummy2 = 10
    else:
            p1 = p2
	    p2 = 11
	    dummy2 = 11
    print "after elifs, p2 = "
    print p2
##    # New p1 is now former p2
##    p1 = no2
##    dummy1 = no2

    # Check to see that new p2 is found in transition matrix. Otherwise, find
    # a new random p2
    while count[p1][p2]['sum'] == 0:
        p2 = random.randint(0,11)
        print "p2 is now random"
        dummy2 = random.randint(0,11)
    print "at very end, p1 ="
    print p1

def write(pch1, pch2, count, song):
        print "write start"
	# Position in measure
	l = 0

	# Initalize measure
	m = music21.stream.Measure()

        #make some dummies
	dummy1 = pch1
	dummy2 = pch2

        #write four quarter notes
	for i in range(4):
        writepitch(dummy1, dummy2, m, count)
        print "following are dummy1, dummy2, and count[][]"
        print dummy1
        print dummy2
        print count[dummy1][dummy2]


##	# For each possible position in measure
##	while l < 4:
##		
##            #write a pitch for each space in the measure
##            writepitch(dummy1, dummy2, m, count)
##            l += 1

        #write measure to song
    song.append(m)
        #print "write finished"
            
