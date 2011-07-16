#!/usr/bin/env python

# bbt.py v0.1b - BlackBerry BBThumbsXXXxXXX.key file parser
# Copyright (C) 2011, Sheran A. Gunasekera <sheran@zensay.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#
# Warning: There is no error checking and no verification if the file read is actually a thumbs.key file

import sys
import struct
import datetime


def usage():
	print("Usage: bbt.py <bbthumbs key file>")
	sys.exit(0)

if(len(sys.argv) < 2 or len(sys.argv) > 3):
	usage()

print "*** Processing "+sys.argv[1]+" on "+str(datetime.datetime.now())
bbt_file = open(sys.argv[1],'rb')
bbt_file.seek(13,0)
thumbs = {}

try:
	while(True):
		tkey = (struct.unpack(">4s",bbt_file.read(4)))[0].encode("hex").upper()
		bbt_file.seek(4,1)
		tval = str(struct.unpack(">I",bbt_file.read(4))[0])
		thumbs[tkey] = tval 
except:
	bbt_file.close()
	for key in thumbs.iterkeys():
		print "Record id "+key+" is at offset "+thumbs[key]
	print "*** Read "+str(len(thumbs.keys()))+" records"
