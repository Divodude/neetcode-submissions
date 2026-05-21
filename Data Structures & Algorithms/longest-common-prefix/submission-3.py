class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        idx=0
        matching=True
        if len(strs)==1:
            return strs[0]
        while matching:
            if idx>=len(strs[0]):
                break
            prev=strs[0][idx]
            for i in strs:
                if idx>len(i)-1:
                    matching=False
                    break
                if prev!=i[idx]:
                    matching=False
                    break
                print(prev)
                prev=i[idx]
            if matching:
                idx+=1

        
       
        return strs[0][:idx]
    
