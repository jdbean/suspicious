#!/usr/bin/python -i
from optparse import OptionParser
import os
import re
import sys
import datetime

parser = OptionParser()

(options, args) = parser.parse_args()

report = dict()
file
for a in args:
	summaryfile = open(a)
	
	#sample input
	#../bzr.lf/lsb/devel/build_env/headers/x86-64/4.1/glib-2.0/gio/gmenuexporter.h.defs(1): export(1);
	for line in summaryfile:
		#find the file name which is before the matching parathsis before the last colon on the line
		filename = line[:line[:line.rfind(':')].rfind('(')]
		#find the total number of words found by locating the end of the filename and taking the number in parathesis right before the :
		totalfilecount = line[line[:line.rfind(':')].rfind('(')+1:line[:line.rfind(':')].rfind(')')]
		#find the list of words following the :, and split them by the ;, and then drop the last item on the list which is always a \n
		foundwords = line[line.rfind(':')+1:].split(';')[:-1]
		report[filename] = dict()		
		for w in foundwords:
			w = w.strip()
			word = w[:w.find('(')]
			wcount = w[w.find('(')+1:w.find(')')]		
			report[filename][word] = wcount

