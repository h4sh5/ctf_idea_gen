#!/usr/bin/env python3

import random

category_file = 'categories.txt'
words_file = 'words.txt'

categories = open(category_file,'r').read().split('\n')
categories.remove('')
words = open(words_file,'r').read().split('\n')
words.remove('')

while True:
	input('next? ')
	# choose 1 category and 2 words
	#cat = random.choice(categories)
	word1 = random.choice(words)
	word2 = random.choice(words)
	word3 = random.choice(words)
	print(word1, word2, word3)
