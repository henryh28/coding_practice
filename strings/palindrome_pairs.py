def palindromePairs(self, words):
	"""
	:type words: List[str]
	:rtype: List[List[int]]
	"""
	test = {value: index for index, value in enumerate(words)}
	answer = []

	for key, value in test.items():
	  length = len(key)
	  for i in range(length + 1):
	    prefix = key[:i]
	    suffix = key[i:]

	    if prefix == prefix[::-1]:
	      target = suffix[::-1]
	      if target in test and target != key:
	        answer.append([test[target], value])

	    if i != length and suffix == suffix[::-1]:
	      target = prefix[::-1]
	      if target in test and target != key:
	        answer.append([value, test[target]])

	return (answer)
