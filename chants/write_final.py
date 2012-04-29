####################### DIATONICHWRITE3.PY #########################

# Generates music file based on most probable path
# of pitches of notes (order 3) and durations of notes (order 2)
# For 3-note chains, 4 quarter notes per measure
# Includes hidden state capability, though only one of the three
# hidden states made here is used in this implementation.
# Only writes songs in the major or harmonic minor modes

import random
import music21

noteList = ['C','C#','D','E-','E','F','F#', 'G','G#','A','B-','B']
dList = ['16th', 'eighth', 'quarter', 'half', 'whole']

p1 = random.randint(0,11)
p2 = random.randint(0,11)
p = random.randint(0,11)
d = random.randint(0,4)
state = 'h1'
mode = 'major'
key = 0
firstmodal = True

# Define transition probabilities between hidden states (to be determined
# empirically, from training data). For this implementation, only use
# hidden state 'h1'.
hiddens = {'h1': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0},
           'h2': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0},
           'h3': {'h1': 1.0, 'h2': 0.0, 'h3': 0.0}}


# Function writes first measure, followed by all others
def writer(countmatrix2, countmatrix3, countd, songstream, num_measures):
    global d
    
    #Write first measure
    writefirst(countmatrix2, countmatrix3, countd, songstream)
    
    #Write as many other measures as desired
    for i in range(num_measures-1):
        write(countmatrix2, countmatrix3, countd, songstream, d)


# Function picks a note based on a given probability distribution.
# Simply a way of consolidating messy sections of code. 
def pickanote(countmatrices, order):

    print "pickanote"

    # Define global variables
    global p1
    global p2

    looper = True

    holdp1 = p1
        
    while looper:

        # Make random number between 0 and 1
        r = random.random()
        
        # Use order two transition probabilities to find a second note given
      # a first
        if order == 2:            
            if r <= countmatrices[2][p1][0]:
                p1 = 0
                modemaker(p1)
                    # In each case, check to see if mode needs to be see
            elif r > countmatrices[2][p1][0] and r <= countmatrices[2][p1][1]:
                p1 = 1
                modemaker(p1)
            elif r > countmatrices[2][p1][1] and r <= countmatrices[2][p1][2]:
                p1 = 2
                modemaker(p1)
            elif r > countmatrices[2][p1][2] and r <= countmatrices[2][p1][3]:
                p1 = 3
                modemaker(p1)
            elif r > countmatrices[2][p1][3] and r <= countmatrices[2][p1][4]:
                p1 = 4
                modemaker(p1)
            elif r > countmatrices[2][p1][4] and r <= countmatrices[2][p1][5]:
                p1 = 5
                modemaker(p1)
            elif r > countmatrices[2][p1][5] and r <= countmatrices[2][p1][6]:
                p1 = 6
                modemaker(p1)
            elif r > countmatrices[2][p1][6] and r <= countmatrices[2][p1][7]:
                p1 = 7
                modemaker(p1)
            elif r > countmatrices[2][p1][7] and r <= countmatrices[2][p1][8]:
                p1 = 8
                modemaker(p1)
            elif r > countmatrices[2][p1][8] and r <= countmatrices[2][p1][9]:
                p1 = 9
                modemaker(p1)
            elif r > countmatrices[2][p1][9] and r <= countmatrices[2][p1][10]:
                p1 = 10
                modemaker(p1)
            else:
                p1 = 11
                modemaker(p1)
                    
            # Checks for ugly note intervals
            if holdp1 == 0 and (p1 == 11 or p1 == 10):
                looper = True
            elif holdp1 == 11 and p1 == 0:
                looper = True
            elif holdp1 == 10 and p1 == 0:
                looper = True
            # Forces chosen note to be in diatonic scale, or else will
          # loop once more
            elif (p1 - key)%12 == 0:
                looper = False
            elif ((p1 - key)%12 == 2):
                looper = False
            elif (mode == 'minor' and (p1 - key)%12 == 3):
                looper = False
            elif (mode == 'major' and (p1 - key)%12 == 4):
                looper = False
            elif (p1 - key)%12 == 5:
                looper = False
            elif (p1 - key)%12 == 7:
                looper = False
            elif (mode == 'minor' and (p1 - key)%12 == 8):
                looper = False
            elif (mode == 'major' and (p1 - key)%12 == 9):
                looper = False
            elif (p1 - key)%12 == 11:
                looper = False
            else:
                p1 = holdp1
                

        # Use order 3 transition probabilities to find a third note given two.
      # In case a given two-state has no possible transitions from it, use the
      # order 2 model. 
        elif order == 3 and (p2 not in countmatrices[3][p1]):
            p1 = p2
            if r <= countmatrices[2][p1][0]:
                    p2 = 0
                    modemaker(p2)
            elif r > countmatrices[2][p1][0] and r <= countmatrices[2][p1][1]:
                    p2 = 1
                    modemaker(p2)
            elif r > countmatrices[2][p1][1] and r <= countmatrices[2][p1][2]:
                    p2 = 2
                    modemaker(p2)
            elif r > countmatrices[2][p1][2] and r <= countmatrices[2][p1][3]:
                    p2 = 3
                    modemaker(p2)
            elif r > countmatrices[2][p1][3] and r <= countmatrices[2][p1][4]:
                    p2 = 4
                    modemaker(p2)
            elif r > countmatrices[2][p1][4] and r <= countmatrices[2][p1][5]:
                    p2 = 5
                    modemaker(p2)
            elif r > countmatrices[2][p1][5] and r <= countmatrices[2][p1][6]:
                    p2 = 6
                    modemaker(p2)
            elif r > countmatrices[2][p1][6] and r <= countmatrices[2][p1][7]:
                    p2 = 7
                    modemaker(p2)
            elif r > countmatrices[2][p1][7] and r <= countmatrices[2][p1][8]:
                    p2 = 8
                    modemaker(p2)
            elif r > countmatrices[2][p1][8] and r <= countmatrices[2][p1][9]:
                    p2 = 9
                    modemaker(p2)
            elif r > countmatrices[2][p1][9] and r <= countmatrices[2][p1][10]:
                    p2 = 10
                    modemaker(p2)
            else:
                    p2 = 11
                    modemaker(p2)

            # Screens for ugly note intervals (major and minor sevenths)
            if p1 == 0 and (p2 == 11 or p2 == 10):
                looper = True
            elif p1 == 11 and p2 == 0:
                looper = True
            elif p1 == 10 and p2 == 0:
                looper = True
            # Forces chosen note to be in diatonic scale, or else will
          # loop once more
            elif (p2 - key)%12 == 0:
                looper = False
            elif ((p2 - key)%12 == 2):
                looper = False
            elif (mode == 'minor' and (p2 - key)%12 == 3):
                looper = False
            elif (mode == 'major' and (p2 - key)%12 == 4):
                looper = False
            elif (p2 - key)%12 == 5:
                looper = False
            elif (p2 - key)%12 == 7:
                looper = False
            elif (mode == 'minor' and (p2 - key)%12 == 8):
                looper = False
            elif (mode == 'major' and (p2 - key)%12 == 9):
                looper = False
            elif (p2 - key)%12 == 11:
                looper = False
            else:
                p2 = p1
                p1 = holdp1
                
        # As long as transitions for the 2-state exist,
      # the new p1 becomes the old p2. Second, the new p2 is
      # assigned a value according to the transition probabilities            
        else:
            if r <= countmatrices[3][p1][p2][0]:
                    p1 = p2
                    p2 = 0
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][0] and r <= countmatrices[3][p1][p2][1]:
                    p1 = p2
                    p2 = 1
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][1] and r <= countmatrices[3][p1][p2][2]:
                    p1 = p2
                    p2 = 2
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][2] and r <= countmatrices[3][p1][p2][3]:
                    p1 = p2
                    p2 = 3
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][3] and r <= countmatrices[3][p1][p2][4]:
                    p1 = p2
                    p2 = 4
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][4] and r <= countmatrices[3][p1][p2][5]:
                    p1 = p2
                    p2 = 5
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][5] and r <= countmatrices[3][p1][p2][6]:
                    p1 = p2
                    p2 = 6
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][6] and r <= countmatrices[3][p1][p2][7]:
                    p1 = p2
                    p2 = 7
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][7] and r <= countmatrices[3][p1][p2][8]:
                    p1 = p2
                    p2 = 8
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][8] and r <= countmatrices[3][p1][p2][9]:
                    p1 = p2
                    p2 = 9
                    modemaker(p2)
            elif r > countmatrices[3][p1][p2][9] and r <= countmatrices[3][p1][p2][10]:
                    p1 = p2
                    p2 = 10
                    modemaker(p2)
            else:
                    p1 = p2
                    p2 = 11
                    modemaker(p2)

            # First if statement keeps note from being repeated more than twice
          # in a row
            if p1 == holdp1 and (p2 - p1)%key == 0:
                looper = True
            # Checks for ugly intervals, makes sure note is diatonic
            elif p1 == 0 and (p2 == 11 or p2 == 10):
                looper = True
            elif p1 == 11 and p2 == 0:
                looper = True
            elif p1 == 10 and p2 == 0:
                looper = True
            elif (p2 - key)%12 == 0:
                looper = False
            elif ((p2 - key)%12 == 2):
                looper = False
            elif (mode == 'minor' and (p2 - key)%12 == 3):
                looper = False
            elif (mode == 'major' and (p2 - key)%12 == 4):
                looper = False
            elif (p2 - key)%12 == 5:
                looper = False
            elif (p2 - key)%12 == 7:
                looper = False
            elif (mode == 'minor' and (p2 - key)%12 == 8):
                looper = False
            elif (mode == 'major' and (p2 - key)%12 == 9):
                looper = False
            elif (p2 - key)%12 == 11:
                looper = False
            else:
                p2 = p1
                p1 = holdp1


# Function checks whether this is first instance of "modal" note -- a sixth
# or third -- and sets mode accordingly
def modemaker(newpit):

    print "modemaker"

    global firstmodal
    global mode
    
    if firstmodal == True and ((newpit-key)%12 == 3 or (newpit-key)%12 == 8):
        mode = 'minor'
        firstmodal = False
    elif firstmodal == True and ((newpit-key)%12 == 4 or (newpit-key)%12 == 9):
        firstmodal = False


# Writes first measure. All transition matrices should be passed in as
# arguments. 
def writefirst(countmat2, countmat, countd, mysong):

    print "writefirst"

    global p1
    global p2
    global state
    global key
    global d

    #print "writefirst started"

    # Define emission probabilities from each hidden state.
  # These are defined locally since the names of the transition matrices
  # are not global.
    emissions = {'h1': {2: countmat2, 3: countmat}, 'h2': {}, 'h3': {}}

    # Define probabilities of starting in any given state
    starting_probs = {'h1': 1.0, 'h2': 0.0, 'h3': 0.0}

    # Choose first note pitch and duration based on random number, save it as key of piece
    n1 = music21.note.Note(noteList[p1])
    key = p1
    n1.duration.type = dList[d]

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
    pickd(countd, d)
    
    n2 = music21.note.Note(noteList[p1])
    n2.duration.type = dList[d]

    # Initialize and write to measure 
    m = music21.stream.Measure()

    m.append(n1)
    m.append(n2)

    # Make sure p1 and p2 reflect first two notes
    p2 = p1
    p1 = key

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
    pickd(countd, d)
    
    # Write two more notes in measure to make a four-note measure
    writepitch(m, countmat, countmat2, countd, d)
    writepitch(m, countmat, countmat2, countd, d)

    #write measure to song
    mysong.append(m)

    #print "writefirst done"
  
def writepitch(msr,counts, counts2, countd, d):

    print "writepitch"

    # Definition of global variables. 
    global p1
    global p2
    global state

    emissions = {'h1': {2: counts2, 3: counts}, 'h2': {}, 'h3': {}}

    # Create note with p2 pitch and quarter duration
    pit2 = noteList[p2]
    n2 = music21.note.Note(pit2)
    n2.duration.type = dList[d]

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
    pickd(countd, d)
    

def write(countm2, countm, countmd, songs, countd, d):

    print "write"

        #print "write start"
  # Position in measure
    l = 0

    # Initalize measure
    m = music21.stream.Measure()

        #write four quarter notes
    for i in range(4):
            writepitch(m, countm, countm2, countd, d)

        #write measure to song
    songs.append(m)

def pickd(countd, d):

    print "pickd"

    # Pick a duration based on probability matrix for duration
    r2 = random.random()
        # print r
      #'32nd','16th', 'eighth', 'quarter', 'half', 'whole'
      
    if r2 <= countd[d][0]:
        d = 0
            #d = '16th'
    elif r2 > countd[d][0] and r2 <= countd[d][1]:
        d = 1
            #d = 'eighth'
    elif r2 > countd[d][1] and r2 <= countd[d][2]:
        d = 2
            #d = 'quarter'
    elif r2 > countd[d][2] and r2 <= countd[d][3]:
        d = 3
            #d = 'half'
    else:
        d = 4
            #d = 'whole'
 