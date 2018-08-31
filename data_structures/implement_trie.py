class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        """ Insert 'word' in to Trie """
        current = self.root

        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        
        current.is_word = True
                

    def search(self, word, starts_with_mode = False):
        """ Checks if 'word' is in Trie """
        current = self.root
        
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
          
        return (current.is_word) if starts_with_mode == False else True

      
    def startsWith(self, prefix):
        """ Checks if word starting with 'prefix' is in Trie """
        return self.search(prefix, True)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)