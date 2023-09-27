#!/usr/bin/env python3

# Read TSV and write as TXT

tsv_file = "input.tsv"
txt_file = "output.txt"

with open(tsv_file, "r") as tsv, open(txt_file, "w") as txt:
    for line in tsv:
        txt.write(line.replace("\t", " "))

import sys

for line in sys.stdin:
	words = line.split()
	for word in words:
		print('(0)\t{1}'.format(word,1))
