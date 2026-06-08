class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit=set()
        path=set()
        self.ans=True
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent):
            visit.add(node)


            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei,node)
                elif nei!=parent:
                    self.ans=False
                    return 

        dfs(0,-1)
        if len(visit) != n:
            return False
        return self.ans

        