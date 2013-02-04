#NYT Corpus Helpers

Helper functions for processing [New York Times Corpus](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2008T19).

*   ___dollarSignSentences(folder)___ 
	* Extracts sentences containing '$' sign	from New York Times Corpus.
*	___writeSentences(outFile, sentences)___
	* Write sentences (one per line) from the list to the file.
*	___filterSentences(keyword, sentences)___
	* Filters list of sentences by keyword.
*	___printRandomSentences(number, sentences)___
	* Prints 'number' of randomly picked sentences from the list.
*	___filterSentencesByLength(min, max, number, sentences)___
	* Prints 'number' of sentences of length between min and max.
*	___extractIntoFile(keyword, outFile, sentences)___
	* Finds sentences containing keyword and write it to the file.
*	___pos(sentence)___
	* Assign part-of-speech to words in sentence.
*	___graphChunks(sentence)___
	* Draws a graph of noun chunks.