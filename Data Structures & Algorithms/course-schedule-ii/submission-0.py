class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        que=[]
        adj=[[] for _ in range(numCourses)]
        self.ans=[]

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
            self.ans.append(node)
            return True
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i,set()):
                    return []
        return self.ans[::-1]