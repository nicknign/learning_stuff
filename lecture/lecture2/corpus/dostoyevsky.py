import io
import os
import ast

"""
Load the cornell movie dialog corpus.

Available from here:
http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

"""

class FictionData:

	def __init__(self, dirName):
		"""
		Args:
		dirName (string): directory where to load the corpus
		"""
		
		fileNames = ['2638-0.txt', '28054-0.txt','pg600.txt']

		self.corpus = []
		for filename in fileNames:
			self.corpus.append(self.loadLines(dirName + filename))

		self.filterChars()

	def loadLines(self, fileName):
		"""
		Args:
			fileName (str): file to load
		Return:
			list<unicode-char>: the document content loaded into list of characters
		"""
		lines = []
		with open(fileName, 'r') as f:
			for line in f:
			 lines.append(line)

		words = []
		for i in range(len(lines)):
			if lines[i] == '\n':
				if i==0 or lines[i-1] != '\n':
					words.extend(list(lines[i]))
			elif lines[i].endswith('\n'):
				words.extend(list(lines[i][:-1]))
				words.append(' ')

		return words

	def filterChars(self):
		from collections import Counter
		c = Counter(self.corpus[0])
		for i in range(1, len(self.corpus)):
			c.update(Counter(self.corpus[i]))

		def isalnum_(c):
			if c>='a' and c<='z':
				return True
			if c>='A' and c<='Z':
				return True
			if c>='0' and c<='9':
				return True
			return False
			
		del_keys = []
		for k in c.keys():
			if (not isalnum_(k)) and c[k] < 100:
				del_keys.append(k)

		for k in del_keys:
			del c[k]

		print('valid keys are %s' % repr(c.keys()))


if __name__ == '__main__':
	fiction = FictionData(dirName = '../data/dostoyevsky/')

