import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for frm, to, price in flights:
            adj[frm].append((to, price))

        pq = [(0, src, 0)]
        dist = [[float('inf')] * (k + 2) for _ in range(n)]

        while pq:
            price, sour, destin = heapq.heappop(pq)

            if sour == dst:
                return price

            if destin == k + 1:
                continue

            for nei, wt in adj[sour]:
                if price + wt < dist[nei][destin + 1]:
                    dist[nei][destin + 1] = price + wt
                    heapq.heappush(pq, (price + wt, nei, destin + 1))

        return -1
