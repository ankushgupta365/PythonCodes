class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adja = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            adja[crs].append(preq)
        
        visit = set()
        path = set()
        res = []
        #topological sort
        def dfs(crs):
            if crs in path:
                return False
            if crs in visit:
                return True
            path.add(crs)
            for preq in adja[crs]:
                if not dfs(preq):
                    return False
            path.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


        