class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        map=defaultdict(list)
        for u,v in tickets:
            map[u].append(v)
    
        order=[]
        for src in map:
            map[src].sort()
            
        def dfs(node):
            
            while map[node]:
                nei=map[node].pop(0)
                dfs(nei)
            order.append(node)
        dfs("JFK")
        return order[::-1]
        