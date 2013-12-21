import os
from array import array
from subprocess import *

#BLACKLIST
# 'Counter\ 2',
#'Timer', 
# the current files cause the convert.py script to completely hang
qtzfolder = "Origami-demos"
qtzfilenames = ['Bouncy\ Animation', 'Button', 'Classic\ Animation', 'Color\ Transition', 'Hit\ Area', 'Image\ Transition', 'Image\ With\ Shadow', 'Layer', 'Phone\ Dimensions', 'Phone', 'Rectangle', 'Scroll', 'Shadow\ Components', 'Shadow\ Info', 'Switch', 'Text\ Layer', 'Transition', 'Value\ or\ Default', 'Value\ to\ Boolean']
outputfolder = "Origami-test-output"

for f in qtzfilenames :
	print f
	print call("python convert.py "+qtzfolder+"/"+f+".qtz > "+outputfolder+"/"+f+".html", shell=True)
	
quit()