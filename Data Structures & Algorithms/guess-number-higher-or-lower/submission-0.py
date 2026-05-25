
class Solution:
    def guessNumber(self, n: int) -> int:
        start=1
        end=n

        while start<=end:
            mid=(start+end)//2
            if guess(mid)==0:
                return mid
            elif guess(mid)==-1:
                end=mid-1
            elif guess(mid)==1:
                start=mid+1
        return 0
        
