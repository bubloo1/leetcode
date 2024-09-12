
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currCharNode = self.root

        for char in word:
            i = ord(char) - ord('a')
            if currCharNode.children[i] == None:
                currCharNode.children[i] = TrieNode()
            currCharNode = currCharNode.children[i]
        currCharNode.end = True


    def search(self, word: str) -> bool:
        currCharNode = self.root

        for char in word:
            i =  ord(char) - ord('a')
            if currCharNode.children[i] == None:
                return False
            currCharNode = currCharNode.children[i]
        return currCharNode.end
        

    def startsWith(self, prefix: str) -> bool:
        currCharNode = self.root

        for char in prefix:
            i =  ord(char) - ord('a')
            if currCharNode.children[i] == None:
                return False
            currCharNode = currCharNode.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)