class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adja = {i: [] for i in range(numCourses)}   #{0: [], 1: [], 2: [], ......} 
        for crs, prq in prerequisites:     #adjacency representation
            adja[crs].append(prq)

        #topological sorting
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if adja[crs] == []:
                return True
            visit.add(crs)
            for preq in adja[crs]:
                if not dfs(preq): return False
            #removing from path and clearing if no loop detected so far 
            visit.remove(crs)
            adja[crs] = []
            return True
            
        #checking for every set of graph
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        

        
        