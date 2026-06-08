class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        
        n=len(edges)
     
        adj=[[]for _ in range(n+1)]
        def dfs(node,parent):
            visit.add(node)

            for nei in adj[node]:
                if nei not in visit:
                    if not dfs(nei,node):
                        return False
                elif nei!=parent:
                    return False
            return True
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit=set()
            if not dfs(u,-1):
                return [u,v]