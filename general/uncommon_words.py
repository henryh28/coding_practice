class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        hash_a, hash_b = {}, {}
        answer = []

        # Reusable method to find uncommon words in a hash table
        def find_uncommon(hash_table):
          temp = []
          
          for key, value in hash_table.items():
            if value == 1:
              temp.append(key)
          
          return(temp)
        
        # split the 2 strings into 2 dictionaries
        for word in A.split():
          hash_a[word] = 1 if word not in hash_a else hash_a[word] + 1

        for word in B.split():
          hash_b[word] = 1 if word not in hash_b else hash_b[word] + 1

        for key, value in hash_a.items():
          if key not in hash_b and value == 1:
            answer.append(key)
          
        for key, value in hash_b.items():
          if key not in hash_a and value == 1:
            answer.append(key)

        return (answer)
        