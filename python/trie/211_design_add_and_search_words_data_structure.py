
class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        currCharNode = self.root

        for char in word:
            if char not in currCharNode.children:
                currCharNode.children[char] = TrieNode()
            currCharNode = currCharNode.children[char]
        currCharNode.end = True
        

    def search(self, word: str) -> bool:
      
        def dfs(index,currCharNode):

            for i in range(index,len(word)):
                if word[i] == ".":
                    for childNode in currCharNode.children.values():
                        if dfs(i+1,childNode):
                            return True
                    return False
                else:
                    if word[i] not in currCharNode.children:
                        return False
                    currCharNode = currCharNode.children[word[i]]
            return currCharNode.end

        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)