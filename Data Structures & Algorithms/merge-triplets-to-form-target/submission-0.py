class Solution:
    def mergeTriplets(self, triplet: List[List[int]], target: List[int]) -> bool:
        skip=[]
        for i in range(len(triplet)):
            trip=triplet[i]
            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                skip.append(i)
        query=[0,0,0]
        for j in range( len(triplet)):
            if j in skip :
                continue
            trip=triplet[j]
            query=[max(query[0],trip[0]),max(query[1],trip[1]),max(query[2],trip[2])]

        if query==target:
            return True
        return False