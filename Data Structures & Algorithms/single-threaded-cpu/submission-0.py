class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        arr=[]
        for idx,(eq,pr) in enumerate(tasks):
            arr.append([eq,pr,idx])
        arr.sort()
        i=0
        n=len(arr)
        time=0
        result=[]
        que=[]
        while i<n or que:
            if not que and time < arr[i][0]:
                time = arr[i][0]


            while i<n and arr[i][0]<=time:
                heapq.heappush(que,(arr[i][1],arr[i][2]))
                i+=1
            pr,idx=heapq.heappop(que)
            time+=pr
            result.append(idx)
        return result
            
               






