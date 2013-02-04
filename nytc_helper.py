#!/usr/bin/python
# -*- coding: utf-8 -*-

# =============================================================================
#  Author: Jenda Rybak | University of West Bohemia
# =============================================================================

# New York Times Corpus helper functions.

# natural language processing framework
import nltk

# regular expresions
import re

# pathnames
from glob import glob

# xml parser
from xml.dom.minidom import parseString

# time measuring
import time

# random numbers
import random


def dollarSignSentences(folder):
	""" 
	Extracts sentences containing '$' sign
	from New York Times Corpus.

	Keyword arguments:
	folder    -- Folder with NY Times Corpus.

    Return list of sentences.

	"""
	months = glob(folder)
	start_time = time.time()	
	start_seq = "<block class=\"full_text\">"
	end_seq = "</block>"
	# list of sentences
	filtered = list()
	for month in months:
		# Load days folders
		days = glob(month + "/*")
		for day in days:
			# Inform users about current day folder
			print "Processing: " + day
			# Read day files
			files = glob(day + "/*")
			for file in files:
				#open xml file, read and close
				file = open(file,'r')
				data = file.read()
				file.close()
				start = data.find(start_seq);
				if (start > -1):
					# extract just the article block
					start += len(start_seq)
					end = data.find(end_seq, start, len(data));
					data = data[start:end]
					# try to fin $ sign, clean text and tokenize
					if (data.find("$")):
						data = data.replace("<p>", " ")
						data = data.replace("</p>", " ")
						data = data.replace("''", "\"")
						data = data.replace("\n", " ")
						data = " ".join(data.split())
						sentences = nltk.sent_tokenize(data);
						# Filter sentences
						for sentence in sentences:
							if (sentence.find("$") > -1): 
								filtered.append(sentence)
	# Measure time
	print time.time() - start_time, " seconds"
	return filtered



def writeSentences(outFile, sentences):
	"""
	Writes sentences (one per line) from the 
	list to the file.

    Keyword arguments:
    outFile    -- Output file
    sentences  -- List of sentences

    """
	f = open(outFile, "w")
	for sentence in sentences:
		f.writelines(sentence + '\n')
	f.close()
	

def filterSentences(keyword, sentences):
	"""
	Filters list of sentences by keyword.

    Keyword arguments:
    keyword    -- Keyword to find
    sentences  -- List of sentences

    Return list of sentences.

	"""
	result = list()
	for s in sentences:
		if (s.find(keyword) > -1):
			result.append(s)
	print '%d found sentences.' % len(result)
	return result


def printRandomSentences(number, sentences):
	"""
	Prints 'number' of randomly picked sentences
	from the list.

    Keyword arguments:
    number     -- Number of sentences to print
    sentences  -- List of sentences

	"""
	for i in range(number):
		r = random.randint(1, len(sentences)-1)
		print sentences[r] + "\n\n"
		
		
def filterSentencesByLength(min, max, number, sentences):
	"""
	Prints 'number' of sentences of length between min and max.

    Keyword arguments:
    min     -- Minimal sentence length
    max  	-- Maximal sentence length
	number	-- Number of sentences to return
	sentences -- List of sentences

    Return list of sentences.

	"""
	i = y = 0
	result = list()
	while i < number:
		if (len(sentences[i+y]) > min & len(sentences[i+y]) < max):
				result.append(sentences[i+y])
				i += 1
		y += 1	
	return result
		

def extractIntoFile(keyword, outFile, sentences):
	"""
	Finds sentences containing keyword and write it
	to the file.

    Keyword arguments:
	keyword    -- Keyword to find    
    outFile    -- Output file
    sentences  -- List of sentences

    Return list of sentences.

	"""	
	found = sf(" "+ keyword + " ", sentences)
	writeSentences(outFile, found)
	print '%d found sentences.' % len(found)	


def pos(sentence):
	"""
	Assign part-of-speech to words in sentence.

    Keyword arguments:
    sentence  -- One sentence

    Return list annotated sentence.

	"""
	words = nltk.word_tokenize(sentence)
	pos	= nltk.pos_tag(words)
	return pos


def graphChunks(sentence):
	"""
	Draws a graph of noun chunks.

    Keyword arguments:
    sentence  -- One sentence

	"""	
	grammar = "NP: {<DT>?<JJ>*<NN>}" 
	cp = nltk.RegexpParser(grammar) 
	result = cp.parse(sentence) 
	result.draw()




