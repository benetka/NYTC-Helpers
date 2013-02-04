#NYT Corpus Helpers

Helper functions for processing [New York Times Corpus](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2008T19).

*   dollarSignSentences(folder) 
	* Extracts sentences containing '$' sign	from New York Times Corpus.
*	writeSentences(outFile, sentences)
	* Write sentences (one per line) from the list to the file.
*	filterSentences(keyword, sentences):	
	* Filters list of sentences by keyword.
*	printRandomSentences(number, sentences)
	* Prints 'number' of randomly picked sentences from the list.
*	filterSentencesByLength(min, max, number, sentences)	
	* Prints 'number' of sentences of length between min and max.
*	extractIntoFile(keyword, outFile, sentences)
	* Finds sentences containing keyword and write it to the file.
*	pos(sentence)
	* Assign part-of-speech to words in sentence.
*	graphChunks(sentence)
	* Draws a graph of noun chunks.