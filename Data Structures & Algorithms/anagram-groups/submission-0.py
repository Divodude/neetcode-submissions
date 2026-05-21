class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        h_map=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            h_map[key].append(i)
        ans=[]
        for j in h_map:
            ans.append(h_map[j])
        return ans
            
        