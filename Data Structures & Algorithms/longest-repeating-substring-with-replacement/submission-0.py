class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        dic=defaultdict(int)
        longl=0
        l=0
        
        for r in range(len(s)):

            dic[s[r]]+=1
            while sum(dic.values())-max(dic.values())>k and l<=r:
                dic[s[l]]-=1
                l+=1
            longl=max(longl, sum(dic.values()))
        return longl

        