#!/usr/bin/env python3

# Read TSV and write as TXT

tsv_file = "input.tsv"
txt_file = "output.txt"

with open(tsv_file, "r") as tsv, open(txt_file, "w") as txt:
    for line in tsv:
        txt.write(line.replace("\t", " "))

import sys
curr_word =None
curr_count = 0

for line in sys.stdin:
	word,count = line.split('\t')
	count = int(count)
	if word==curr_word:
		curr_count +=count
	else:
		if curr_word:
			print('[0]\t{1}'.format(curr_word, curr_count)
		curr_word = word
		curr_count = count
if curr_word == word:
	print('{0}\t{1}'.format(curr_word, cur_count))

