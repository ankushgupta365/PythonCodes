class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)   #to create a dictionary with empty list 
        wordList.append(beginWord)
        #adjacency list with pattern eg, hit: *it, h*t, hi* 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        res = 1     #since begin word is starting point so 1 length is starting
        q = deque([beginWord])
        visit = set([beginWord]) 

        #bfs 
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*"+ word[j+1:]  #generating patterns as above
                    for nbr in nei[pattern]:
                        if nbr not in visit:
                            visit.add(nbr)
                            q.append(nbr)
            res+=1
        return 0  #if we did not find any sequence