class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        ans = []
        while True:
            arr.sort()
            count,ch=arr[2]
            if count==0:
                break
            if len(ans)>=2 and ans[-1]==ch and ans[-2]==ch:
                if arr[1][0]==0:
                    break
                ans.append(arr[1][1])
                arr[1][0]-=1
            else:
                ans.append(ch)
                arr[2][0]-=1
        return "".join(ans)
            