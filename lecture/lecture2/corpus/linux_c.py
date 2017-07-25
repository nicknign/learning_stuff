from collections import Counter
data = []
with open('../data/linux_source_code/linux_c.txt',encoding='latin-1') as f:
	for line in f:
		data.append(line)


codes = []
for line in data:
	codes.extend(list(line))
c = Counter(codes)
keys_to_del = [x for x in c.keys() if c[x]<1000]
for k in keys_to_del:
	del c[k]

codes = []
for line in data:
	codes.extend([x for x in list(line) if x in c])

import pickle
with open('../data/linux_source_code/linux_c.pkl', 'wb') as f:
	pickle.dump(codes, f)