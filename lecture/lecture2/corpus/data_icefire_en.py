
"""
Load the ice_and_fire_en fiction corpus.

Downloaded from ...
"""

class IceFireEnData(object):

	def __init__(self, dirName):
		"""
		Args:
			dirName (string): directory where to load the corpus
		"""
		self.dirName = dirName
		self.fileNames = ['001ssb.txt', '002ssb.txt', '003ssb.txt', '004ssb.txt', '005ssb.txt']

		self.corpus = []
		for filename in self.fileNames:
			self.corpus.append(self.load_lines(self.dirName + filename))

		self.filter_chars()

	def load_lines(self, fileName):
		"""
		Args:
			fileName (str): file to load
		Return:
			list<unicode-char>: the document content loaded into list of characters
		"""
		lines = []
		print('reading file %s' % fileName)
		with open(fileName, encoding='latin-1') as f:
			for line in f:
				if line.startswith('Page') and str.isnumeric(line[5:]):
					continue
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

	def filter_chars(self):
		from collections import Counter
		c = Counter(self.corpus[0])
		for i in range(1, len(self.corpus)):
			c.update(Counter(self.corpus[i]))

		print('original keys are %s' % repr(c.keys()))

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

		print('keys to be deleted are %s' % repr(del_keys))

		for k in del_keys:
			del c[k]

		print('filtered keys are %s' % repr(c.keys()))

		for i in range(len(self.corpus)):
			self.corpus[i] = [x for x in self.corpus[i] if x in c]

		translator = {'\x85':'.', '\x91':"'", '\x92':"'", '\x93':'"', '\x94':'"', '\x97':'-'}
		for i in range(len(self.corpus)):
			for j in range(len(self.corpus[i])):
				if self.corpus[i][j] in translator:
					self.corpus[i][j] = translator[self.corpus[i][j]]

	def write_file(self, fileName):
		import pickle
		data = []
		for i in range(len(self.corpus)):
			data.extend(self.corpus[i])
		with open(self.dirName + fileName, 'wb') as f:
			pickle.dump(data, f)

if __name__ == '__main__':
	fiction = IceFireEnData(dirName = '../data/ice_and_fire_en/')
	fiction.write_file('ice_and_fire_en.pkl')
