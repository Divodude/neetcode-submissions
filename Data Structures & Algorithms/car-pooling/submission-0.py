class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[]
        que=[]
        
        for (p,f,t) in trips:

            arr.append((f,t,p))
        arr.sort()
        n=len(arr)       
        i=0
      
        dist=0
        while i<n:


            while que and que[0][0]<=arr[i][0]:
                t,p=heapq.heappop(que)
                capacity+=p
            heapq.heappush(que,(arr[i][1],arr[i][2]))
            capacity-=arr[i][2]
            if capacity<0:
                return False
            i+=1
        return True


            

               