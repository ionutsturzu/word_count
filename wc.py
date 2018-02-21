#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script mimics the wc linux command basic functionalities\n")

parser.add_argument('-l', dest='line', action='store_const', const='l',
		help='Display number of lines\n')

parser.add_argument('-w', dest='word', action='store_const', const='w',
		help='Display number of words\n')

parser.add_argument('-c', dest='charac', action='store_const', const='c',
		help='Display number of characters\n')

args = parser.parse_args()


information = sys.stdin.read()
lines = len(information.split('\n')) - 1
words = len(information.split())
chars = len(information)

if args.line:
	print str(lines)
elif args.word:
	print str(words)
elif args.charac:
	print str(chars)
else:
	print '\t' + str(lines),
	print '\t' + str(words),
	print '\t' + str(chars)
