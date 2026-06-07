class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        que=[]
        adj=[[] for _ in range(numCourses)]

        for u,v in prerequisites:
            adj[v].append(u)
        
        def dfs(node,path):
            if node in path:
                return False
            if node in visit:
                return True
            
            path.add(node)
            for nei in adj[node]:
                if nei not in visit:
                   
                    if not dfs(nei,path):
                        return False
            visit.add(node)
            return True
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i,set()):
                    return False
        return True

        
       