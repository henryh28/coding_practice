def groupAnagrams(self, strs):
  """
  :type strs: List[str]
  :rtype: List[List[str]]
  """
  groups = collections.defaultdict(list)
  answer = []
  
  for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)
    
  for group in groups.values():
    answer.append(group)
  
  return(answer)
  