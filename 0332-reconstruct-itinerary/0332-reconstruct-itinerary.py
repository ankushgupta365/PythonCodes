class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        #constructiong adjacency list representation of the graph in reverse, to make sure we pop least lexical scope destination first
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []

        #go deep into the graph until no destination found from the source, this will ensure that we visit that destion last which don't have any source
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())  #popping least lexical scope airport and visiting it
            itinerary.append(airport)
        

        #kickstart the journey
        dfs("JFK")
        
        return itinerary[::-1]