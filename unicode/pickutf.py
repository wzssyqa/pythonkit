#!/usr/bin/env python
# Copyright 2010 YunQiang Su <wzssyqa@gmail.com>
# Scan a file look for \$\#x1111;  and convert them to a char of utf8
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#

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

