class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        import heapq
        adj=[[] for _ in range(n)]
        for u,v,t in times:
            adj[u-1].append((t,v-1))
        visit=set()
        visit.add(k)
        que=[(0,k-1)]
        

        
        dis=[float("inf")]*n
        dis[k-1]=0
        while que:
            w,node=heapq.heappop(que)
            

            for t,nei in adj[node]:
                if t+w<dis[nei]:
                    dis[nei]=dis[node]+t
                    heapq.heappush(que,(dis[nei],nei))
                   

            
        ans = max(dis)
        return ans if ans != float("inf") else -1
            


        