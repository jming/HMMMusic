#!/usr/bin/python

# Compilation
# CS51 Final Project 2012

from music21 import *

i = 0
s = converter.parse('%i.mid' % (i))

s.show('text')