
# class TrieNode():
#     def __init__(self):
#         self.children = [None] * 26
#         self.end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         currCharNode = self.root

#         for char in word:
#             i = ord(char) - ord('a')
#             if currCharNode.children[i] == None:
#                 currCharNode.children[i] = TrieNode()
#             currCharNode = currCharNode.children[i]
#         currCharNode.end = True


#     def search(self, word: str) -> bool:
#         currCharNode = self.root

#         for char in word:
#             i =  ord(char) - ord('a')
#             if currCharNode.children[i] == None:
#                 return False
#             currCharNode = currCharNode.children[i]
#         return currCharNode.end
        

#     def startsWith(self, prefix: str) -> bool:
#         currCharNode = self.root

#         for char in prefix:
#             i =  ord(char) - ord('a')
#             if currCharNode.children[i] == None:
#                 return False
#             currCharNode = currCharNode.children[i]
#         return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self,sentance):
       
#         currNode = self.root

#         for char in sentance:
#             print(char)
#             if char not in currNode.children:
#                 currNode.children[char] = TrieNode()
#             currNode = currNode.children[char]
#         currNode.end = True
    
#     def search(self,searchWord):
#         searchWord = searchWord.split(" ")
#         # print("search word",searchWord)
#         res = []
#         for word in searchWord:
#             currNode = self.root
#             for char in word:
#                 # print("dfgfgdf",char)
#                 if char not in currNode.children:
#                     # print("break")
#                     break
#                 # print(currNode.end,"fsgfgfg")
#                 if char in currNode.children and currNode.children[char].end == True:
#                     # print("nce")
#                     res.append(searchWord)
#                     break
#                 currNode = currNode.children[char]
#         return res


# newObject = Trie()
# newObject.insert("app")
# print(newObject.search("apple banana apricot blueberry avocado"))