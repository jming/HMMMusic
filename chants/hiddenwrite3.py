####################### HIDDENWRITE3.PY #########################

# Generates music file based on most probable path
# For 3-note chains, 4 quarter notes per measure
# Includes hidden state capability, though only one of the three
# hidden states made here is used in this implementation

import random
import music21

noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']

p1 = random.randint(0,11)
p2 = random.randint(0,11)
p = random.randint(0,11)
state = 'h1'

# Define transition probabilities between hidden states (to be determined
# empirically, from training data). For this implementation, only use
# hidden state 'h1'.
hiddens = {'h1': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0},
           'h2': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0},
           'h3': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0}}


# Function picks a note based on a given probability distribution.
# Simply a way of consolidating messy sections of code. 
def pickanote(countmatrices, order):

    # Define global variables
    global p1
    global p2

    # Make random number between 0 and 1
    r = random.random()
    
    # Use order two transition probabilities to find a second note given
    # a first
    if order == 2:
        if r <= countmatrices[2][p1][0]:
                p1 = 0
        elif r > countmatrices[2][p1][0] and r <= countmatrices[2][p1][1]:
                p1 = 1
        elif r > countmatrices[2][p1][1] and r <= countmatrices[2][p1][2]:
                p1 = 2
        elif r > countmatrices[2][p1][2] and r <= countmatrices[2][p1][3]:
                p1 = 3
        elif r > countmatrices[2][p1][3] and r <= countmatrices[2][p1][4]:
                p1 = 4
        elif r > countmatrices[2][p1][4] and r <= countmatrices[2][p1][5]:
                p1 = 5
        elif r > countmatrices[2][p1][5] and r <= countmatrices[2][p1][6]:
                p1 = 6
        elif r > countmatrices[2][p1][6] and r <= countmatrices[2][p1][7]:
                p1 = 7
        elif r > countmatrices[2][p1][7] and r <= countmatrices[2][p1][8]:
                p1 = 8
        elif r > countmatrices[2][p1][8] and r <= countmatrices[2][p1][9]:
                p1 = 9
        elif r > countmatrices[2][p1][9] and r <= countmatrices[2][p1][10]:
                p1 = 10
        else:
                p1 = 11

    # Use order 3 transition probabilities to find a third note given two.
    # In case a given two-state has no possible transitions from it, use the
    # order 2 model. 
    elif order == 3 and (p2 not in countmatrices[3][p1]):
        p1 = p2
        if r <= countmatrices[2][p1][0]:
                p2 = 0
        elif r > countmatrices[2][p1][0] and r <= countmatrices[2][p1][1]:
                p2 = 1
        elif r > countmatrices[2][p1][1] and r <= countmatrices[2][p1][2]:
                p2 = 2
        elif r > countmatrices[2][p1][2] and r <= countmatrices[2][p1][3]:
                p2 = 3
        elif r > countmatrices[2][p1][3] and r <= countmatrices[2][p1][4]:
                p2 = 4
        elif r > countmatrices[2][p1][4] and r <= countmatrices[2][p1][5]:
                p2 = 5
        elif r > countmatrices[2][p1][5] and r <= countmatrices[2][p1][6]:
                p2 = 6
        elif r > countmatrices[2][p1][6] and r <= countmatrices[2][p1][7]:
                p2 = 7
        elif r > countmatrices[2][p1][7] and r <= countmatrices[2][p1][8]:
                p2 = 8
        elif r > countmatrices[2][p1][8] and r <= countmatrices[2][p1][9]:
                p2 = 9
        elif r > countmatrices[2][p1][9] and r <= countmatrices[2][p1][10]:
                p2 = 10
        else:
                p2 = 11

    # As long as transitions for the 2-state exist,
    # the new p1 becomes the old p2. Second, the new p2 is
    # assigned a value according to the transition probabilities            
    else:
        if r <= countmatrices[3][p1][p2][0]:
                p1 = p2
                p2 = 0
        elif r > countmatrices[3][p1][p2][0] and r <= countmatrices[3][p1][p2][1]:
                p1 = p2
                p2 = 1
        elif r > countmatrices[3][p1][p2][1] and r <= countmatrices[3][p1][p2][2]:
                p1 = p2
                p2 = 2
        elif r > countmatrices[3][p1][p2][2] and r <= countmatrices[3][p1][p2][3]:
                p1 = p2
                p2 = 3
        elif r > countmatrices[3][p1][p2][3] and r <= countmatrices[3][p1][p2][4]:
                p1 = p2
                p2 = 4
        elif r > countmatrices[3][p1][p2][4] and r <= countmatrices[3][p1][p2][5]:
                p1 = p2
                p2 = 5
        elif r > countmatrices[3][p1][p2][5] and r <= countmatrices[3][p1][p2][6]:
                p1 = p2
                p2 = 6
        elif r > countmatrices[3][p1][p2][6] and r <= countmatrices[3][p1][p2][7]:
                p1 = p2
                p2 = 7
        elif r > countmatrices[3][p1][p2][7] and r <= countmatrices[3][p1][p2][8]:
                p1 = p2
                p2 = 8
        elif r > countmatrices[3][p1][p2][8] and r <= countmatrices[3][p1][p2][9]:
                p1 = p2
                p2 = 9
        elif r > countmatrices[3][p1][p2][9] and r <= countmatrices[3][p1][p2][10]:
                p1 = p2
                p2 = 10
        else:
                p1 = p2
                p2 = 11

# Function writes first measure, followed by all others
def writer(countmatrix2, countmatrix3, songstream, num_measures):

    #Write first measure
    writefirst(countmatrix2, countmatrix3, songstream)

    #Write as many other measures as desired
    for i in range(num_measures-1):
        write(countmatrix2, countmatrix3, songstream)
    

# Writes first measure. All transition matrices should be passed in as
# arguments. 
def writefirst(countmat2, countmat, mysong):

    global p1
    global p2
    global state

    # Define emission probabilities from each hidden state.
    # These are defined locally since the names of the transition matrices
    # are not global.
    emissions = {'h1': {2: countmat2, 3: countmat}, 'h2': {}, 'h3': {}}

    # Define probabilities of starting in any given state
    starting_probs = {'h1': 1.0, 'h2': 0.0, 'h3': 0.0}

    # Choose first note based on random number, save it in dummy variable
    n1 = music21.note.Note(noteList[p1])
    dummy = p1

    # Find first state based on starting probabilities
    r1 = random.random()
    if r1 <= starting_probs['h1']:
        state = 'h1'
    elif r1 > starting_probs['h1'] and r1 <= starting_probs['h2']:
        state = 'h2'
    elif r1 > starting_probs['h2'] and r1 <= starting_probs['h3']:
        state = 'h3'

    # Choose second note based on order 2 transitions
    pickanote({2:emissions[state][2], 3: emissions[state][3]},2)

    n2 = music21.note.Note(noteList[p1])

    # Modify duration
    n1.duration.type = 'quarter'
    n2.duration.type = 'quarter'

    # Initialize and write to measure 
    m = music21.stream.Measure()

    m.append(n1)
    m.append(n2)

    # Make sure p1 and p2 reflect first two notes
    p2 = p1
    p1 = dummy

    # Possible change of hidden state, based on hiddens[state]
    # transition probabilities
    r1 = random.random()
    if r1 <= hiddens[state]['h1']:
        state = 'h1'
    elif r1 > hiddens[state]['h1'] and r1 <= hiddens[state]['h2']:
        state = 'h2'
    elif r1 > hiddens[state]['h2'] and r1 <= hiddens[state]['h3']:
        state = 'h3'
    
    # Pick next note based on order 3 transitions
    pickanote({2:emissions[state][2], 3: emissions[state][3]}, 3)
    
    # Write two more notes in measure to make a four-note measure
    writepitch(m, countmat, countmat2)
    writepitch(m, countmat, countmat2)

    #write measure to song
    mysong.append(m)

    print "End of writefirst, p1 = "
    print p1
    print "p2 ="
    print p2

    
def writepitch(msr,counts, counts2):

    # Definition of global variables. 
    global p1
    global p2
    global state

    emissions = {'h1': {2: counts2, 3: counts}, 'h2': {}, 'h3': {}}

    print "writepitch started with p1="
    print p1
    print "p2 = "
    print p2

    # Create note with p2 pitch and quarter duration
    pit2 = noteList[p2]
    n2 = music21.note.Note(pit2)
    n2.duration.type = 'quarter'

    # Add this onto the measure
    msr.append(n2)

    # Possible change of hidden state, based on hiddens[state]
    # transition probabilities
    r1 = random.random()
    if r1 <= hiddens[state]['h1']:
        state = 'h1'
    elif r1 > hiddens[state]['h1'] and r1 <= hiddens[state]['h2']:
        state = 'h2'
    elif r1 > hiddens[state]['h2'] and r1 <= hiddens[state]['h3']:
        state = 'h3'

    #Choose new note
    pickanote({2: emissions[state][2], 3: emissions[state][3]},3)
    
    print "after elifs, p2 = "
    print p2


    print "at very end, p1 ="
    print p1

def write(countm2, countm, songs):
        print "write start"
	# Position in measure
	l = 0

	# Initalize measure
	m = music21.stream.Measure()

        #write four quarter notes
	for i in range(4):
            writepitch(m, countm, countm2)

        #write measure to song
        songs.append(m)
        print "write finished"
            
