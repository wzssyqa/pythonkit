#!/usr/bin/env python
import sys

if sys.argv[1]:
	ifn=sys.argv[1]
if sys.argv[2]:
	ofn=sys.argv[2]
if not ifn or not ofn:
	print 'pickutf inputfile outfile'

infile=open(ifn,'r')
outfile=open(ofn,'w')

while(1):
	c=infile.read(1)
	tmp= c
	if not c:
		break;
	if c=='\\':
		tmp=tmp+infile.read(1)
	if tmp=='\&':
		tmp=tmp+infile.read(3)
	if tmp=='\&\#x':
		uc=unichr(int(infile.read(4),16)).encode('utf8')
		infile.read(1)
		outfile.write(uc)
		continue
	else:
		outfile.write(tmp)	

