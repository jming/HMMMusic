Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.curdir
'.'
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Program Files (x86)\\Python27'
>>> os.chdir('C://Users/Alisa/HMMMusic/chants
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir('C://Users/Alisa/HMMMusic/chants')
>>> os.getcwd()
'C:\\Users\\Alisa\\HMMMusic\\chants'
>>> from music21 import *
music21: Certain music21 functions might need these optional packages: matplotlib, numpy, scipy, PIL; if you run into errors, install it by following the instructions at http://mit.edu/music21/doc/html/installAdditional.html
>>> notes = {}
>>> count = []
>>> count = {}
>>> notes[i] - []

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    notes[i] - []
NameError: name 'i' is not defined
>>> notes[i] = []

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    notes[i] = []
NameError: name 'i' is not defined
>>> i = 0
>>> while i < 60:
	if (i == 33) or (i ==34):
		i +=1
		else:
			
SyntaxError: invalid syntax
>>> while i <60:
	if (i==33 or (i==34):
	    
SyntaxError: invalid syntax
>>> while i < 60:
	if (i == 33) or (i ==34):
		i +=1
		else:
			
SyntaxError: invalid syntax
>>> while i < 60:
	if (i == 33) or (i ==34):
		i +=1
	else:
		notes[i] = []
		s = music21.converter.parse('%i.mid' % (i))
		measures = s[0].measures(1,60)

		

Traceback (most recent call last):
  File "<pyshell#25>", line 6, in <module>
    s = music21.converter.parse('%i.mid' % (i))
NameError: name 'music21' is not defined
>>> import music21
>>> s = music21.converter.parse('0.mid')
>>> measures = s[0].measures(1,60)
>>> measures
<music21.stream.Part 75360968>
>>> for measure in measures:
	for notey in measure.notes:
		notes[i].append(notey)

		
>>> notes
{0: [<music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note C>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note D>]}
>>> notes[0].generalNote.quarterLength

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    notes[0].generalNote.quarterLength
AttributeError: 'list' object has no attribute 'generalNote'
>>> notes[0]
[<music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note C>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note B->, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note D>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note A>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B->, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note E>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note C>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note F>, <music21.note.Note E>, <music21.note.Note G>, <music21.note.Note G>, <music21.note.Note F>, <music21.note.Note D>, <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>, <music21.note.Note D>]
>>> notes[0][0]
<music21.note.Note C>
>>> notes[0][0].generalNote.quarterLength

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    notes[0][0].generalNote.quarterLength
AttributeError: 'Note' object has no attribute 'generalNote'
>>> notes[0][0].duration
<music21.duration.Duration 0.875>
>>> durations = {}
>>> durations[0] = []
>>> for n in notes:
	duration[0].append(n.duration)

	

Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    duration[0].append(n.duration)
TypeError: 'module' object is not subscriptable
>>> for n in notes[0]:
	duration[0].append(n.duration)

	

Traceback (most recent call last):
  File "<pyshell#47>", line 2, in <module>
    duration[0].append(n.duration)
TypeError: 'module' object is not subscriptable
>>> duration[0][0] = notes[0][0].duration

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    duration[0][0] = notes[0][0].duration
TypeError: 'module' object is not subscriptable
>>> duration[0][0] = notes[0][0].duration()

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    duration[0][0] = notes[0][0].duration()
TypeError: 'Duration' object is not callable
>>> duration[0][0] = 0.875

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    duration[0][0] = 0.875
TypeError: 'module' object is not subscriptable
>>> for n in notes[0]:
	durations[0].append(n.duration)

	
>>> durations
{0: [<music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.75>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.75>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.25>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.375>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.375>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.75>, <music21.duration.Duration 0.875>, <music21.duration.Duration 0.875>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.75>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.75>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.25>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.5>, <music21.duration.Duration 1.75>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.375>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.75>, <music21.duration.Duration 0.875>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.375>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.75>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.875>, <music21.duration.Duration 1.75>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 2.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>, <music21.duration.Duration 0.5>, <music21.duration.Duration 2.0>, <music21.duration.Duration 1.0>, <music21.duration.Duration 0.5>]}
>>> durations2 = {}
d
>>> durations2[0] = []
>>> for n in durations[0]:
	durations2[0].append(n.


		0
			     
SyntaxError: invalid syntax
>>> for n in notes[0]:
	durations2[0].append(n.duration.quarterLengthToClosestType())

	

Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    durations2[0].append(n.duration.quarterLengthToClosestType())
AttributeError: 'Duration' object has no attribute 'quarterLengthToClosestType'
>>> for n in notes[0]:
	durations2[0].append(music21.duration.quarterLengthToClosestType(n.duration.quarterLength))

>>> 
>>> durations2
{0: [('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', False), ('16th', True), ('quarter', True), ('eighth', True), ('16th', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', True), ('16th', False), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('eighth', False), ('quarter', False), ('eighth', False), ('eighth', False), ('eighth', False), ('quarter', True), ('half', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('half', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', False), ('quarter', True), ('eighth', False), ('eighth', False), ('quarter', True), ('half', True), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('eighth', False), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('quarter', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', True), ('16th', False), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', True), ('quarter', False), ('eighth', False), ('eighth', True), ('16th', False), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', False), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', False), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', False), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True)]}
>>> durations3 = {}
>>> durations3[0] = []
>>> for n in notes[0]:
	durations3[0].append(music21.duration.convertQuarterLengthToType(n.duration.quarterLength))

	

Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    durations3[0].append(music21.duration.convertQuarterLengthToType(n.duration.quarterLength))
  File "C:\Program Files (x86)\Python27\lib\site-packages\music21\duration.py", line 265, in convertQuarterLengthToType
    raise DurationException("cannot convert quarterLength %s exactly to type" % qLen)
DurationException: cannot convert quarterLength 0.875 exactly to type
>>> falses = 0
>>> falses = []
>>> for d in durations2[0]:
	for e in d:
		falses.append(e)

		
>>> falses
['eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', False, '16th', True, 'quarter', True, 'eighth', True, '16th', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', True, '16th', False, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'eighth', False, 'quarter', False, 'eighth', False, 'eighth', False, 'eighth', False, 'quarter', True, 'half', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'half', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', False, 'quarter', True, 'eighth', False, 'eighth', False, 'quarter', True, 'half', True, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'eighth', False, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'quarter', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', True, '16th', False, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', True, 'quarter', False, 'eighth', False, 'eighth', True, '16th', False, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', False, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', False, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', False, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True]
>>> filter
<built-in function filter>
>>> falses.length

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    falses.length
AttributeError: 'list' object has no attribute 'length'
>>> falses.sort
<built-in method sort of list object at 0x00000000044A64C8>
>>> falses.sort()
>>> falses
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, '16th', '16th', '16th', '16th', '16th', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'eighth', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'half', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter']
>>> length(falses)

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    length(falses)
NameError: name 'length' is not defined
>>> fs = []
>>> fs = filter(lambda x: isinstance(x,'False'), falses)

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    fs = filter(lambda x: isinstance(x,'False'), falses)
  File "<pyshell#87>", line 1, in <lambda>
    fs = filter(lambda x: isinstance(x,'False'), falses)
TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
>>> fs = filter(lambda x: x = 'False', falses)
SyntaxError: lambda cannot contain assignment
>>> fs = 0
>>> for f in falses:
	if f = 'False':
		
SyntaxError: invalid syntax
>>> for f in falses:
	if f = 'False':
		
SyntaxError: invalid syntax
>>> for f in falses:
	if f == 'False':
		fs+=1

		
>>> fs
0
>>> for f in falses:
	if f == False:
		fs+=1

		
>>> fs
53
>>> ts = 0
>>> for t in falses:
	if t == True:
		ts+=1

		
>>> ts
175
>>> durations3
{0: []}
>>> durations2
{0: [('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', False), ('16th', True), ('quarter', True), ('eighth', True), ('16th', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', True), ('16th', False), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('eighth', False), ('quarter', False), ('eighth', False), ('eighth', False), ('eighth', False), ('quarter', True), ('half', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('half', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', False), ('quarter', True), ('eighth', False), ('eighth', False), ('quarter', True), ('half', True), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('quarter', False), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('eighth', False), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('quarter', False), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', True), ('16th', False), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('quarter', False), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('eighth', False), ('quarter', False), ('eighth', True), ('quarter', False), ('eighth', False), ('eighth', True), ('16th', False), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', False), ('quarter', True), ('eighth', False), ('quarter', True), ('quarter', True), ('eighth', False), ('quarter', True), ('eighth', False), ('quarter', False), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', False), ('eighth', True), ('quarter', True), ('half', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', False), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('quarter', True), ('quarter', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True), ('eighth', True), ('half', True), ('quarter', True), ('eighth', True)]}
>>> d2 = []
>>> for d in durations2[0]:
	for e in d:
		d2.append(e)

		
>>> d2
['eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', False, '16th', True, 'quarter', True, 'eighth', True, '16th', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', True, '16th', False, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'eighth', False, 'quarter', False, 'eighth', False, 'eighth', False, 'eighth', False, 'quarter', True, 'half', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'half', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', False, 'quarter', True, 'eighth', False, 'eighth', False, 'quarter', True, 'half', True, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'quarter', False, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'eighth', False, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'quarter', False, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', True, '16th', False, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'quarter', False, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'eighth', False, 'quarter', False, 'eighth', True, 'quarter', False, 'eighth', False, 'eighth', True, '16th', False, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', False, 'quarter', True, 'eighth', False, 'quarter', True, 'quarter', True, 'eighth', False, 'quarter', True, 'eighth', False, 'quarter', False, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', False, 'eighth', True, 'quarter', True, 'half', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', False, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'quarter', True, 'quarter', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True, 'eighth', True, 'half', True, 'quarter', True, 'eighth', True]
>>> d2 = filter(lambda x: isinstance(x,str),d2)
>>> d2
['eighth', 'quarter', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'eighth', 'half', 'eighth', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'half', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'half', 'quarter', '16th', 'quarter', 'eighth', '16th', 'eighth', 'quarter', 'quarter', 'eighth', '16th', 'quarter', 'eighth', 'quarter', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'quarter', 'eighth', 'eighth', 'eighth', 'quarter', 'half', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'quarter', 'half', 'eighth', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'quarter', 'half', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'eighth', 'quarter', 'half', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', '16th', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'eighth', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'eighth', 'eighth', '16th', 'quarter', 'half', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'eighth', 'quarter', 'eighth', 'quarter', 'half', 'quarter', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'quarter', 'half', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'quarter', 'quarter', 'quarter', 'eighth', 'eighth', 'half', 'quarter', 'eighth', 'eighth', 'half', 'quarter', 'eighth']
>>> d2 = map(lambda x: if x =='16th':3 x == 'eighth': 4 else if x == 'quarter': 5 else if x=='half': 6 else if x=='whole': 7,d2)
SyntaxError: invalid syntax
>>> for i in d2:
	
KeyboardInterrupt
>>> d2 = map(lambda x: if x =='16th':3 else if x == 'eighth': 4 else if x == 'quarter': 5 else if x=='half': 6 else if x=='whole': 7,d2)
SyntaxError: invalid syntax
>>> for i in d2:
	if x =='16th':3 else if x == 'eighth': 4 else if x == 'quarter': 5 else if x=='half': 6 else if x=='whole': 7
	
SyntaxError: invalid syntax
>>> nums = []
>>> for i in d2:
	if x =='16th':nums[3]+=1 else if x == 'eighth': nums[4]+=1 else if x == 'quarter': nums[5]+=1 else if x=='half': nums[6]+=1 else if x=='whole': nums[7]+=1
	
SyntaxError: invalid syntax
>>> for i in d2:
	if x =='16th':nums[3]+=1 else if x == 'eighth': nums[4]+=1 else if x == 'quarter': nums[5]+=1 else if x=='half': nums[6]+=1 else if x=='whole': nums[7]+=1
	
SyntaxError: invalid syntax
>>> for xin d2:
	if x =='16th':nums[3]+=1
	
SyntaxError: invalid syntax
>>> for x in d2:
	if x =='16th':nums[3]+=1
	else if x == 'eighth': nums[4]+=1
	
SyntaxError: invalid syntax
>>> for x in d2:
	if x =='16th':nums[3]+=1
	elif x == 'eighth': nums[4]+=1 elif x == 'quarter': nums[5]+=1 elif x=='half': nums[6]+=1 elif x=='whole': nums[7]+=1
	
SyntaxError: invalid syntax
>>> for x in d2:
	if x =='16th':nums[3]+=1
	elif x == 'eighth': nums[4]+=1
	elif x == 'quarter': nums[5]+=1
	
KeyboardInterrupt
>>> for x in d2:
	if x =='16th':nums[3]+=1
	elif x == 'eighth': nums[4]+=1
	elif x == 'quarter': nums[5]+=1
	elif x=='half': nums[6]+=1
	elif x=='whole': nums[7]+=1

	

Traceback (most recent call last):
  File "<pyshell#131>", line 3, in <module>
    elif x == 'eighth': nums[4]+=1
IndexError: list index out of range
>>> nums = [0,0,0,0,0,0,0,0,0,0]
>>> for x in d2:
	if x =='16th':nums[3]+=1
	elif x == 'eighth': nums[4]+=1
	elif x == 'quarter': nums[5]+=1
	elif x=='half': nums[6]+=1
	elif x=='whole': nums[7]+=1

	
>>> nums
[0, 0, 0, 5, 87, 114, 22, 0, 0, 0]
>>> 