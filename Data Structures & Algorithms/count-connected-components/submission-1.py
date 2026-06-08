class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visit=set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count=0

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)     
        for i in range(n):
            if i not in visit:
                count+=1
                dfs(i)
        return count