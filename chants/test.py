noteList = [0,1,2,3,4,5,6,7,8,9,10,11]

countmatrix = [[0]*12]*12

n = 0
m = 0

for note in noteList: 
    countmatrix[note.pitchClass] +=1