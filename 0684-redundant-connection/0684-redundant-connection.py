class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]   #[0,1,2,3,4,5,6], by default every one is parent of iteself
        rank = [1] * (len(edges)+1)    #[1, 1, 1,1,1,], by default every one have rank 1

        def find(n):
            p = par[n]
            #optimizing parents of node to top parent
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        #union find data structure
        def union(n1, n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False      #first loop
            if rank[p1]>rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p2]+= rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                #first loop detected then return
                return [n1, n2]
        