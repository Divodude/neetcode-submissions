class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        left=0
        right=n-1
        idx=0
        i=0
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==x:
                idx=mid
                break
            elif arr[mid]<x:
                idx=mid
                left=mid+1
            else:
                right=mid-1
        f=idx+1
        b=idx
        if x<arr[0]:
            b=-1
            f=0
        if x>arr[n-1]:
            b=n-1
            f=n
            
        ans=[]
        INF=float("inf")

    
        while k>0:
            fwd = INF
            bwd = INF
            if f<n:
                fwd=abs(arr[f]-x)
            if b>=0:
                bwd=abs(arr[b]-x)

            if fwd<bwd and f<n:
                ans.append(arr[f])
                k-=1
                f+=1
            elif bwd<=fwd and b>=0:
                ans.append(arr[b])
                k-=1
                b-=1
            
           
            
        return sorted(ans)

            





        