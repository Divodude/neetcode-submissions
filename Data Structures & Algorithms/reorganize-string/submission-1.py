class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import defaultdict
        def ctn(a):
            return ord(a) - ord('a') 

        que=[]
        h_map=defaultdict(int)
        for i in s:
            h_map[i]+=1
        for j in h_map:
            heapq.heappush(que,(-h_map[j],j))
        if -que[0][0]>(len(s)+1)//2:
            return ""

        result=""
        n=len(s)
        ans=["_"]*n
        pos=0
        
        while que:
            count,ch=heapq.heappop(que)
            count=-count

            
            for _ in range(count):
                if pos>=len(s):
                    pos=1
            
                ans[pos]=ch
                pos+=2
        return "".join(ans)
            


            
