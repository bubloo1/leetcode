from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0
    
    def insertWord(self,word):
        currNode = self

        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
            currNode.refs += 1
        currNode.end = True
    
    def removeWord(self,word):
        
        curr = self
        curr.refs -= 1
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                curr.refs -= 1
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insertWord(word)
        
        rows,cols = len(board), len(board[0])
        res = visited = set()

        def dfs(r,c,node,word):
            if (r not in range(rows) or c not in range(cols) 
                or board[r][c] not in node.children or (r,c) in visited or 
                node.children[board[r][c]].refs < 1):
                return 
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                node.end = False
                res.add(word)
                root.removeWord(word)
        
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)

newObject  = Solution()

print(newObject.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))