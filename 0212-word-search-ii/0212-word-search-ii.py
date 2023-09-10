"""
    1.) Construct the Trie for the words
    2.) For each word in board, check in a backtracking way if word is found in trie, if yes add it to the result and prune it from the Trie(remvoe refs to it)
    3.) Maintain visited and result set and lastly after visiting each and every possibility convert result into list and return
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.refs = 0
    def addWord(self, word):
        curr = self
        curr.refs+=1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.refs+=1
        curr.end = True
    def removeWord(self,word):
        curr = self
        curr.refs-=1
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                curr.refs-=1
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        Rows, Cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r,c,node, word):
            if (r not in range(Rows) or c not in range(Cols) or board[r][c] not in node.children or node.children[board[r][c]].refs < 1 or (r,c) in visited):
                return 
            word += board[r][c]
            visited.add((r,c))
            node = node.children[board[r][c]]
            if node.end:
                node.end = False
                result.add(word)
                root.removeWord(word)
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r,c))
        

        for r in range(Rows):
            for c in range(Cols):
                dfs(r,c,root, "")

        return list(result)
