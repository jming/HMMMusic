#!/usr/bin/python

# Compilation
# CS51 Final Project 2012

# Before running this script, call:
# from music21 import *

i = 0
j = 0

import array
import compare 

notes = {}
count = {}

# Create an array of note sequences for each song
while i < 60:
	if (i == 33) or (i == 34):
		i += 1
	else:
		array.array( i, notes )
		i += 1

# Map probabilities of note transitions for all songs
while j < 60:
	if (j == 33) or (j == 34):
		j += 1
	else:
		compare.compare( j, count, notes )
		j += 1