class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
        print(dic)
        for j in t:
            dic[j]-=1
        print(dic)

        for k in dic:
            if dic[k]!=0:
                return False
        return True


        