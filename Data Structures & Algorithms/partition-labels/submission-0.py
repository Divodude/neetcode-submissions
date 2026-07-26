class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=0
        seqend=0
 
        n=len(s)
        idx={}
        for i in range(n):
            idx[ s[i]]=i
        ids=0
        ans=[]
        while  ids<n:
            seqend=max(seqend,idx[s[ids]])
            if ids==seqend:
                ans.append(seqend-start+1)
                
                start=seqend+1
            ids+=1
        return ans




        