class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans=[]
        def comb(i,arr): 
            if len(arr)==k:
                self.ans.append(arr.copy())
                return 
            if i>=n+1 or len(arr)>k:
                return 
            arr.append(i)
            comb(i+1,arr)
            arr.pop()
            comb(i+1,arr)
        comb(1,[])
        return self.ans


        